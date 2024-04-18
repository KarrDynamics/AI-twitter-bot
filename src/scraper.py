import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

def scrape_website(url):
    print(f"Scraping website: {url}")  # Logging the URL being scraped
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract text content (you can modify this part based on the structure of your website)
    paragraphs = []
    for paragraph in soup.find_all('p'):
        paragraphs.append({"content": paragraph.get_text()})
    
    # Create 'scraped_sites' folder if it doesn't exist
    if not os.path.exists('scraped_sites'):
        os.makedirs('scraped_sites')
    
    # Generate output filename based on URL and timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"scraped_sites/{url.replace('https://', '').replace('/', '_')}_{timestamp}.json"

    # Write the scraped content to a JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(paragraphs, file, indent=4)

    print(f"Scraped content saved to {output_file}")

if __name__ == '__main__':
    url = 'https://www.yourdomain.com'
    scrape_website(url)
