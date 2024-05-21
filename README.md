# AI Twitter Bot

An intelligent Twitter bot that scrapes content from specified websites and generates engaging tweets using OpenAI.

## Features

- **Web Scraping**: Scrape content from specified URLs.
- **AI-Powered Tweet Generation**: Use OpenAI's GPT model to generate tweets based on scraped content.
- **Tweeting Functionality (Coming Soon)**: Integration with Twitter API for automated tweeting is currently under development.
- **Express Server**: Serve the application with a Node.js Express server.
- **Responsive UI**: Modern UI with Bootstrap to enter URLs and display generated tweets.

## Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/KarrDynamics/AI-Twitter-Bot.git
    ```

2. **Install Python Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Node.js Dependencies**
    ```bash
    cd server
    npm install
    ```

4. **API Keys Setup**
    - Create a `.env` file in the root directory.
    - Add your OpenAI API key to the `.env` file:
        ```
        OPENAI_API_KEY=your_openai_api_key_here
        ```

5. **Run the Express Server**
    ```bash
    cd server
    node server.js
    ```

6. **Open the Application**
    - Open your web browser and navigate to `http://localhost:5000`.
    - Enter a URL in the input field and click "Generate Tweets" to see the generated tweets displayed on the page.

## Project Structure

- **src/**: Contains the Python scripts for scraping and generating tweets.
  - `scraper.py`: Scrapes the specified URL for content.
  - `ai_assistant.py`: Uses OpenAI to generate tweets from scraped content.
  - `run_bot.py`: Runs the scraper and tweet generation scripts sequentially.

- **server/**: Contains the Node.js Express server files.
  - `server.js`: Main server file that serves the frontend and handles API requests.

- **public/**: Contains the frontend HTML file.
  - `index.html`: The main HTML file for the frontend interface.

- **.env**: Environment variables file (not included in the repository, to be created by the user).

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
