import json
from datetime import datetime
from openai import OpenAI
import os
import time
import logging

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

# Retrieve OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Generate response using OpenAI
def generate_response(prompt):
    try:
        print("Generating response...")
        start_time = time.time()
        
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        elapsed_time = time.time() - start_time
        print(f"Response generated in {elapsed_time:.2f} seconds.")
        
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error generating response: {e}")
        return None

# Load latest scraped data from JSON file
def fetch_latest_json_file(directory):
    # Get all JSON files in the directory
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

    # Sort files based on timestamp in filename
    json_files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)

    if json_files:
        latest_file = json_files[0]
        print(f"Latest JSON file: {latest_file}")
        return os.path.join(directory, latest_file)
    else:
        print("No JSON files found in the directory.")
        return None

# Load scraped data from JSON file
def load_data(filename):
    print("Loading data...")
    start_time = time.time()
    
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Data loaded successfully in {time.time() - start_time:.2f} seconds.")
        return data
    except json.JSONDecodeError:
        print(f"Error loading {filename}: File is empty or not in valid JSON format.")
        return None

# Generate tweets using OpenAI
def generate_tweets(scraped_data, url):
    # Combine the content from the scraped data into a single string
    combined_content = ' '.join(item['content'] for item in scraped_data)
    
    # Break the combined content into smaller chunks to fit within the API's token limit
    chunk_size = 1000
    content_chunks = [combined_content[i:i + chunk_size] for i in range(0, len(combined_content), chunk_size)]
    
    tweets = []
    
    for i, chunk in enumerate(content_chunks, 1):
        print(f"Sending batch {i} of {len(content_chunks)}...")
        
        prompt = f"Create single tweets with a max of 140 words using the website data:\n{chunk}"
        tweet_text = generate_response(prompt)
        
        if tweet_text:
            tweets.append(tweet_text)
    
    # Generate a filename based on the URL and current date and time
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    # Extract the domain from the URL for the filename
    domain = url.split('//')[-1].split('/')[0]
    filename = f'tweets/{domain}_{timestamp}.json'
    
    with open(filename, 'w') as file:
        json.dump(tweets, file, indent=4)
    
    print(f"Tweets saved to {filename}")

def extract_url_from_filename(filename):
    # Extract the URL from the filename (assumed to be before the timestamp)
    parts = filename.split('_')
    if len(parts) > 1:
        return '_'.join(parts[:-1])
    return 'unknown_url'

if __name__ == '__main__':
    start_time = time.time()
    
    # Fetch the latest scraped data file
    directory = 'scraped_sites'
    latest_file = fetch_latest_json_file(directory)
    
    if latest_file:
        # Load the latest scraped data
        scraped_data = load_data(latest_file)
        
        if scraped_data:
            # Extract URL from the filename
            url = extract_url_from_filename(latest_file)
            print(f"Extracted URL: {url}")  # Debugging line
            
            print("Generating tweets...")
            # Generate tweets
            generate_tweets(scraped_data, url)
    
    print(f"Script executed in {time.time() - start_time:.2f} seconds.")