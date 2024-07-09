# Real Estate Web Application

## Project Overview

This project is a comprehensive real estate web application that includes a frontend for user interactions, a backend for managing data and business logic, an analytics module for market insights, and a scraper for fetching property data from various sources.

### Components

1. **Frontend:** Built with React.js, it provides an interactive UI for users.
2. **Backend:** Built with FastAPI, it handles data storage, user authentication, and business logic.
3. **Analytics:** Analyzes real estate data to provide market insights.
4. **Scraper:** Fetches property details from different websites and stores them in the database.

## Functionalities

- User Registration and Authentication
- Viewing and Searching Property Listings
- Real-time Market Analytics
- Data Scraping from External Sources

## Running the Project Locally

### Prerequisites

- Docker

### Setup Instructions

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/jainalertusa/hackathon-2024.git
    ```

2. **Build and Start the Docker Containers:**
    ```sh
    docker-compose up --build
    ```

3. **Access the Application:**
    - Frontend: `http://localhost:3000`
    - Backend: `http://localhost:8000`
    - Analytics: Check the relevant port specified in the `docker-compose.yml`

### Running the Scraper Locally

1. **Navigate to the Scraper Directory:**
    ```sh
    cd scraper
    ```

2. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Scraper:**
    - Update `zipcodes.txt` with the relevant zip codes you want to scrape data for.
    - Execute the scraper script:
    ```sh
    python crawlers/redfin_scraper.py
    ```

4. **Central Server:**
    - Navigate to the `server` directory and run the central server:
    ```sh
    cd server
    python central_server.py
    ```

## License

This project is licensed under the MIT License
