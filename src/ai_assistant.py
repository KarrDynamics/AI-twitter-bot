import json
import sys
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating response: {e}", file=sys.stderr)
        return None

def generate_tweets(scraped_data):
    combined_content = ' '.join(item['content'] for item in scraped_data)
    
    # Adjust prompt to request exactly 4 tweets
    prompt = f"Create 4 separate tweets using the following website data:\n{combined_content}"
    tweet_text = generate_response(prompt)
    
    # Assuming the response is a string with tweets separated by newlines or other delimiters
    if tweet_text:
        tweets = [tweet.strip() for tweet in tweet_text.split('\n') if tweet.strip()]
        return tweets[:4]  # Ensure only 4 tweets are returned

    return []

if __name__ == '__main__':
    try:
        scraped_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error loading JSON input: {e}", file=sys.stderr)
        sys.exit(1)
    
    if scraped_data:
        tweets = generate_tweets(scraped_data)
        print(json.dumps(tweets))
    else:
        print("No data scraped.", file=sys.stderr)
        sys.exit(1)
