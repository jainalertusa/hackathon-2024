# Apartment Analytics Project

This project consists of a web application that scrapes apartment data, processes it, and displays it via a frontend interface. The backend provides an API for fetching data and generating PDF reports with the property analytics data and a prediction if it is an investable property or not.

## Project Structure

- `backend/`: FastAPI backend application.
    endpoint details:
        1. 


- `frontend/`: React frontend application.
- `scraper/`: Python script to scrape apartment data.
- `analytics/`: Python script to process scraped data.
- `docker-compose.yml`: Docker Compose configuration.
- `README.md`: Project documentation.

## Setup and Run

1. Clone the repository:
   ```bash
   git clone https://github.com/snshahgit/Module-1.git
   cd Module-1

2. Build and run the project using Docker Compose:
    docker-compose up --build

3. Access the frontend application at `http://localhost:3000`

4. Access the backend application at `http://localhost:8000`