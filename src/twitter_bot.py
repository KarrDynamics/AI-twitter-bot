import json
import os
import logging
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Function to fetch tweets from JSON file
def fetch_tweets(filename):
    logging.info(f"Fetching tweets from {filename}...")
    with open(filename, 'r') as file:
        data = json.load(file)
    if isinstance(data, list):
        return data
    else:
        logging.error("Expected a list but got something else.")
        return []

# Fetch tweets
tweets = fetch_tweets("tweets/tweets_20240418_130525.json")
logging.info(f"Fetched tweets: {tweets}")

# Post the first tweet
if tweets:
    tweet = tweets[0]
    logging.info(f"Posting tweet: {tweet}")

    # OAuth 1.0 credentials
    consumer_key = os.getenv('TWITTER_API_KEY')
    consumer_secret = os.getenv('TWITTER_API_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    # Create an OAuth1Session
    twitter_session = OAuth1Session(consumer_key, client_secret=consumer_secret,
                                    resource_owner_key=access_token,
                                    resource_owner_secret=access_token_secret)

    # Tweet data
    data = {
        "text": tweet
    }

    # Make POST request
    response = twitter_session.post(
        "https://api.twitter.com/2/tweets",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 201:
        logging.info("Tweet posted successfully!")
    else:
        logging.error(f"Error posting tweet: {response.json()}")

else:
    logging.warning("No tweets to post.")
