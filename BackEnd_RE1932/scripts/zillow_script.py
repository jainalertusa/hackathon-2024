import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define the URL of the Redfin property page you want to scrape
property_url = "https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/address?postalcode=90815&page=1&pagesize=100"

headers = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'apikey' : '2b1e86b638620bf2404521e6e9e1b19e'})

# Send an HTTP request to the property page and retrieve the HTML content
response = requests.get(property_url, headers=headers)

print(response.json())

# Parse the HTML content using