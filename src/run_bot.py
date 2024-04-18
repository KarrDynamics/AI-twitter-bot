import subprocess

def run_script(script_name):
    try:
        print(f"Starting {script_name}.py...")
        subprocess.run(['python', f'src/{script_name}.py'], check=True)
        print(f"{script_name}.py completed.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}.py: {e}")
        return False

if __name__ == "__main__":
    print("Initializing bot execution...")

    # Run scraper.py
    scraper_success = run_script("scraper")

    # Run ai_assistant.py after scraper.py is done
    if scraper_success:
        print("\nRunning ai_assistant.py...")
        run_script("ai_assistant")
    
    print("\nBot execution completed. Website scraped and Tweets generated. 🎉")
