import requests
from bs4 import BeautifulSoup
import pandas as pd  

import csv
import schedule
import time

# Function to scrape data and save to CSV
def scrape_to_csv():
    # Replace 'YourUserAgentString' with your actual user agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
    }
    query = 'Artificial Intelligence'
    url = f'https://www.bing.com/search?q={query}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data
    links = [link.get('href') for link in soup.find_all('a')]
    meta_tags = [str(tag) for tag in soup.find_all('meta')]
    title_tags = [str(soup.find('title'))]

    # Save data to CSV
    with open('search_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Links', 'Meta Tags', 'Title Tags'])
        writer.writerows(zip(links, meta_tags, title_tags))
    scrape_to_csv()
  