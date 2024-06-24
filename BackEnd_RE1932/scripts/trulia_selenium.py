import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def extract(city, num_pages=500):
    results = []

    # Using Firefox WebDriver. You can use other drivers as well.
    driver = webdriver.Firefox()

