# Real Estate Project

## Overview

This project is a comprehensive real estate platform consisting of several microservices:

•⁠  ⁠*Frontend*: A React-based user interface.
•⁠  ⁠*Backend*: A FastAPI-based service providing RESTful APIs.
•⁠  ⁠*Analytics*: Data processing and analysis using Python.
•⁠  ⁠*Scraper*: A web scraping service to collect real estate data.

## Project Structure

real-estate/
├── analytics
│ ├── analytics.py
│ ├── Dockerfile
│ └── requirements.txt
├── backend
│ ├── app
│ │ ├── init.py
│ │ ├── database.py
│ │ ├── main.py
│ │ ├── models.py
│ │ ├── schemas.py
│ │ └── utils.py
│ ├── Dockerfile
│ └── requirements.txt
├── frontend
│ ├── public
│ │ └── index.html
│ ├── src
│ │ ├── App.jsx
│ │ ├── index.css
│ │ ├── index.js
│ │ └── components
│ │ ├── MyComponent.css
│ │ └── MyComponent.jsx
│ ├── Dockerfile
│ └── package.json
├── scraper
│ ├── central_server.py
│ ├── Dockerfile.scraper
│ ├── Dockerfile.server
│ ├── docker-compose.yaml
│ ├── mongodb_connection.py
│ ├── requirements.txt
│ ├── scraper.py
│ └── zipcodes.txt
├── docker-compose.yml
└── README.md


## Getting Started

### Prerequisites

•⁠  ⁠Docker
•⁠  ⁠Docker Compose

### Running the Project

1.⁠ ⁠Clone the repository:
    ⁠ bash
    git clone <repository-url>
    cd real-estate
     ⁠

2.⁠ ⁠Build and run the services:
    ⁠ bash
    docker-compose up --build
     ⁠

3.⁠ ⁠Access the frontend at ⁠ http://localhost:3000 ⁠ and backend at ⁠ http://localhost:8000 ⁠.

## Services

### Frontend

•⁠  ⁠*Location*: ⁠ frontend/ ⁠
•⁠  ⁠*Technology*: React
•⁠  ⁠*Port*: 3000

### Backend

•⁠  ⁠*Location*: ⁠ backend/ ⁠
•⁠  ⁠*Technology*: FastAPI
•⁠  ⁠*Port*: 8000

### Analytics

•⁠  ⁠*Location*: ⁠ analytics/ ⁠
•⁠  ⁠*Technology*: Python
•⁠  ⁠*Port*: (not exposed)

### Scraper

•⁠  ⁠*Location*: ⁠ scraper/ ⁠
•⁠  ⁠*Technology*: Python
•⁠  ⁠*Port*: (not exposed)

## Presentation Video 
https://drive.google.com/file/d/10rkfOfxwzUUGGvOChSap9Ccv5dqn5PF5/view?usp=drive_link

## License

This project is licensed under the MIT License.
