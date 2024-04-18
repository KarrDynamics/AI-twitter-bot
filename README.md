# AI Twitter Bot

An intelligent Twitter bot that scrapes content from specified websites and generates engaging tweets using OpenAI.

## Features

- **Web Scraping**: Scrape content from specified URLs.
- **AI-Powered Tweet Generation**: Use OpenAI's GPT model to generate tweets based on scraped content.
- **Tweeting Functionality (Coming Soon)**: Integration with Twitter API for automated tweeting is currently under development.

## Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/KarrDynamics/AI-Twitter-Bot.git
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **API Keys Setup**
    - Create a `.env` file in the root directory.
    - Add your OpenAI API key to the `.env` file:
        ```
        OPENAI_API_KEY=your_openai_api_key_here
        ```

4. **Specify URL in `scraper.py`**
    - Open `scraper.py`.
    - Replace the `url` variable with the desired URL you want to scrape.

5. **Run the Bot**
    ```
    python src/run_bot.py
    ```

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.



Note: This 