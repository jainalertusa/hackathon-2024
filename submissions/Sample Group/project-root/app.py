from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup
import random
import time
import logging
import csv
import math
from create_table import db, ScrapedData, create_tables, MedianPPSF

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scraped_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Ensure tables are created
with app.app_context():
    create_tables()

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of user agents for randomization
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1'
]

# Function to extract listings from a given URL
# Similar logic can be used to extract data from other website
def extract_listings(session, url):
    try:
        # Randomize user-agent
        headers = {
            'user-agent': random.choice(user_agents),
            'referer': 'https://www.zillow.com/'
        }

        # Simulate waiting for page load
        time.sleep(random.uniform(5, 10))

        response = session.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        address = [addr.text.strip() for addr in soup.find_all('address', {'data-test': 'property-card-addr'})]
        price = [p.text.strip() for p in soup.find_all('span', {'data-test': 'property-card-price'})]
        seller = [s.text.strip() for s in soup.find_all('div', {'class': 'eWCfWA'})]
        
        # Extracting beds, baths, and sqft
        details = [d.find_all('b') if d.find_all('b') else [] for d in soup.find_all('ul', {'class': 'eRHJK'})]

        rows = []
        for adr, pr, sl, detail_items in zip(address, price, seller, details):
            bd = detail_items[0].text.strip() if detail_items and len(detail_items) > 0 else ''
            ba = detail_items[1].text.strip() if detail_items and len(detail_items) > 1 else ''
            sq = detail_items[2].text.strip() if detail_items and len(detail_items) > 2 else ''
            
            address_parts = adr.split(', ')
            first_line = address_parts[0] if len(address_parts) > 0 else ''
            city = address_parts[1] if len(address_parts) > 1 else ''
            state_zip = address_parts[2].split() if len(address_parts) > 2 else []
            state = state_zip[0] if state_zip else ''
            zip_code = state_zip[1] if len(state_zip) > 1 else ''

            full_address = f"{first_line}; {city}; {state}; {zip_code}"

            # Calculate PPSF
            try:
                if pr and sq:
                    price_per_sqft = round(float(pr.replace(',', '').strip('$')) / float(sq.replace(',', '')),2)
                else:
                    price_per_sqft = None
            except ValueError:
                price_per_sqft = None

            #Calculate score
            try:
                median_ppsf_data = MedianPPSF.query.filter_by(city=city, state=state).first()
                if median_ppsf_data:
                    m_ppsf = median_ppsf_data.m_ppsf
                    if price_per_sqft and m_ppsf:
                        score = calculate_score(price_per_sqft,m_ppsf)
                    else:
                        score = None
                else:
                    score = None

            except Exception as e:
                logging.error(f"Error calculating score for {city}, {state}: {e}")
                score = None

            # Check if address already exists in database
            existing_data = ScrapedData.query.filter_by(full_address=full_address).first()
            if not existing_data:
                # Store in database
                new_data = ScrapedData(
                    first_line=first_line,
                    city=city,
                    state=state,
                    zip_code=zip_code,
                    full_address=full_address,
                    price=pr,
                    seller=sl,
                    beds=bd,
                    baths=ba,
                    sqft=sq,
                    score=score,
                    ppsf=price_per_sqft  # Store PPSF in database
                )
                db.session.add(new_data)
                db.session.commit()

                # Append to rows list for returning to client (not necessary for database operation)
                rows.append({
                    'first_line': first_line,
                    'city': city,
                    'state': state,
                    'zip_code': zip_code,
                    'full_address': full_address,
                    'price': pr,
                    'seller': sl,
                    'beds': bd,
                    'baths': ba,
                    'sqft': sq,
                    'score': score,
                    'ppsf': price_per_sqft  # Include PPSF in returned rows
                })

        return rows, soup

    except requests.exceptions.RequestException as e:
        logging.error(f"Request Exception: {e}")
        return [], None
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        return [], None


def calculate_score(ppsf, m_ppsf):
    try:
        if ppsf and m_ppsf:
            difference = m_ppsf - ppsf

            if difference >= 100:
                score = 10
            elif difference >= 80:
                score = 9
            elif difference >= 60:
                score = 8
            elif difference >= 40:
                score = 7
            elif difference >= 20:
                score = 6
            elif difference >= 0:
                score = 5
            elif difference >= -20:
                score = 4
            elif difference >= -40:
                score = 3
            elif difference >= -60:
                score = 2
            elif difference >= -80:
                score = 1
            else:
                score = 0

        else:
            score = None
    except Exception as e:
        logging.error(f"Error calculating score: {e}")
        score = None

    return score

def add_median_ppsf_data():
    # Check if the data is already populated
    existing_data_count = db.session.query(MedianPPSF.id).count()
    if existing_data_count > 0:
        logging.info("Median PPSF data already exists. Skipping...")
        return
    
    with open('Median_PPSF.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city = row['City']
            state = row['State']
            ppsf_str = row['PPSF']
            
            # Convert PPSF to float, handling empty strings gracefully
            if ppsf_str:
                ppsf = float(ppsf_str.replace('$', '').replace(',', ''))
            else:
                ppsf = 0.0

            # Insert the data into the database
            new_data = MedianPPSF(city=city, state=state, m_ppsf=ppsf)
            db.session.add(new_data)
            db.session.commit()
            #print(f"Added median PPSF data for {city}, {state}")

# Add data when the application starts
@app.before_request
def add_data():
    add_median_ppsf_data()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    return render_template('scrape.html')

@app.route('/start_scraping', methods=['POST'])
def start_scraping():
    # List of all state abbreviations in the USA. For prototype purpose only few added to increase running speed. Do add remaning to scrap data for all over the conutry.
    state_abbreviations = ['MA']
    
    # List to store all rows from all pages
    all_rows = []

    # Set to track seen identifiers (first_line, city, state, zip_code)
    seen_rows = set()

    # Timer and maximum duration
    max_duration = 60  # 100 seconds (adjust as needed)

    with requests.Session() as session:
        for state in state_abbreviations:
            start_time = time.time()
            if time.time() - start_time > max_duration:
                logging.info("Max duration reached. Stopping scraping.")
                break
            
            current_url = f'https://www.zillow.com/{state}/'
            page_number = 1  # Track the current page number
            
            while current_url:
                # Check if max duration exceeded before proceeding to the next page
                if time.time() - start_time > max_duration:
                    logging.info("Max duration reached. Stopping scraping.")
                    break
                
                try:
                    rows, soup = extract_listings(session, current_url)
                    all_rows.extend(rows)

                    logging.info(f"Scraped data for {state} - Page {page_number}")

                    next_button = soup.find('a', {'class': 'StyledButton-c11n-8-101-0__sc-iv7357-0 ehhlLE PaginationButton-c11n-8-101-0__sc-1i6hxyy-0 gSZahV', 'rel': 'next'})
                    if next_button:
                        next_url = 'https://www.zillow.com' + next_button['href']
                        current_url = next_url
                        page_number += 1
                        time.sleep(random.uniform(3, 6))  # Random delay between requests
                    else:
                        current_url = None

                except Exception as e:
                    logging.error(f"Error processing state {state}: {e}")

    logging.info("Scraping complete.")

    return jsonify({'status': 'Scraping completed successfully'})

@app.route('/database', methods=['GET'])
def database():
    city = request.args.get('city', '')
    state = request.args.get('state', '')
    zip_code = request.args.get('zip_code', '')
    price = request.args.get('price', '')
    beds = request.args.get('beds', '')
    baths = request.args.get('baths', '')
    sqft = request.args.get('sqft', '')
    score_min = request.args.get('score_min', '')

    # Query database with filters
    query = ScrapedData.query
    if city:
        query = query.filter(ScrapedData.city.ilike(f'%{city}%'))
    if state:
        query = query.filter(ScrapedData.state.ilike(f'%{state}%'))
    if zip_code:
        query = query.filter(ScrapedData.zip_code.ilike(f'%{zip_code}%'))
    if price:
        query = query.filter(ScrapedData.price.ilike(f'%{price}%'))
    if beds:
        query = query.filter(ScrapedData.beds.ilike(f'%{beds}%'))
    if baths:
        query = query.filter(ScrapedData.baths.ilike(f'%{baths}%'))
    if sqft:
        query = query.filter(ScrapedData.sqft.ilike(f'%{sqft}%'))
    if score_min:
        query = query.filter(ScrapedData.score >= int(score_min))

    rows = query.all()
    return render_template('database.html', rows=rows)


@app.route('/high_score_properties', methods=['GET'])
def high_score_properties():
    city = request.args.get('city', '')
    state = request.args.get('state', '')
    zip_code = request.args.get('zip_code', '')
    price = request.args.get('price', '')
    beds = request.args.get('beds', '')
    baths = request.args.get('baths', '')
    sqft = request.args.get('sqft', '')

    # Query database for properties with score > 8
    query = ScrapedData.query.filter(ScrapedData.score > 8)

    # Apply additional filters
    if city:
        query = query.filter(ScrapedData.city.ilike(f'%{city}%'))
    if state:
        query = query.filter(ScrapedData.state.ilike(f'%{state}%'))
    if zip_code:
        query = query.filter(ScrapedData.zip_code.ilike(f'%{zip_code}%'))
    if price:
        query = query.filter(ScrapedData.price.ilike(f'%{price}%'))
    if beds:
        query = query.filter(ScrapedData.beds.ilike(f'%{beds}%'))
    if baths:
        query = query.filter(ScrapedData.baths.ilike(f'%{baths}%'))
    if sqft:
        query = query.filter(ScrapedData.sqft.ilike(f'%{sqft}%'))

    rows = query.all()
    return render_template('high_score_properties.html', rows=rows, city=city, state=state, zip_code=zip_code, price=price, beds=beds, baths=baths, sqft=sqft)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
