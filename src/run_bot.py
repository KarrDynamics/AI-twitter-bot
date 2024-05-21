import subprocess
import sys
import os
import json

def run_script(script_name, *args, input_data=None):
    try:
        result = subprocess.run(
            ['python', os.path.join(os.path.dirname(__file__), script_name), *args],
            input=input_data,
            text=True,
            capture_output=True,
            check=True
        )
        print(f"Output from {script_name}:\n{result.stdout}", file=sys.stderr)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL to scrape.", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    temp_file = 'temp_tweets.json'

    # Run scraper.py
    scraper_output = run_script("scraper.py", url)

    if scraper_output:
        # Run ai_assistant.py with scraper output as input
        ai_output = run_script("ai_assistant.py", input_data=scraper_output)
        
        if ai_output:
            try:
                tweets = json.loads(ai_output)
                with open(temp_file, 'w') as f:
                    json.dump(tweets, f, indent=4)
                print(f"Tweets saved to {temp_file}")
            except json.JSONDecodeError as e:
                print(f"Error parsing generated tweets: {e}", file=sys.stderr)
                sys.exit(1)
    else:
        print("Error: scraper_output is None", file=sys.stderr)
        sys.exit(1)
