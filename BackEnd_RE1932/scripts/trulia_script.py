import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
# Define the URL of the Redfin property page you want to scrape
property_url = "https://www.trulia.com/NY/New_York/"

headers = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'})

# Send an HTTP request to the property page and retrieve the HTML content
response = requests.get(property_url, headers=headers)
time.sleep(3)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

#result_update = soup.find_all("li", {"class": "Grid__CellBox-sc-a8dff4e9-0 sc-84372ace-0 kloaJl kTTMdB"})

properties = soup.find_all("div", {"data-testid": "property-card-details"})


address = [result.find("div", {"data-testid": "property-address"}).get_text() for result in properties]
beds = [result.find('div', {'data-testid':'property-beds'}).get_text() for result in properties]
baths = [result.find('div', {'data-testid':'property-baths'}).get_text() for result in properties]
prices = [result.find('div', {'data-testid':'property-price'}).get_text() for result in properties]


print(prices)


'''real_estate = pd.DataFrame(columns=['Address', 'Beds', 'Baths', 'Price'])
for i in range(len(address)):
    real_estate = real_estate.append({'Address': address[i], 'Beds': beds[i], 'Baths': baths[i], 'Price': prices[i]},
                                     ignore_index=True)

print(real_estate)'''
''' '# Extract specific information from the property page
property_address = soup.find("span", class_="street-address").text
property_price = soup.find("span", class_="statsValue").text
property_photos = [img["src"] for img in soup.find_all("img", class_="photo-tile")]

# Print the extracted information
print(f"Property Address: {property_address}")
print(f"Property Price: {property_price}")
print(f"Property Photos: {property_photos}") '''
