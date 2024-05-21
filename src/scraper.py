import requests
from bs4 import BeautifulSoup
import json
import sys

def scrape_website(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {response.status_code}", file=sys.stderr)
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    paragraphs = []
    for paragraph in soup.find_all('p'):
        paragraphs.append({"content": paragraph.get_text()})
    
    return paragraphs

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a URL to scrape.", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    scraped_data = scrape_website(url)
    
    if scraped_data:
        print(json.dumps(scraped_data))
    else:
        sys.exit(1)
