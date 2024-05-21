const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 5000;
const TEMP_FILE = path.join(__dirname, 'temp_tweets.json');

app.use(cors());
app.use(express.json());

app.use(express.static(path.join(__dirname, '../frontend')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/index.html'));
});

app.post('/api/generate-tweets', (req, res) => {
  const { url } = req.body;
  if (!url) {
    return res.status(400).json({ error: 'URL is required' });
  }

  const runBot = spawn('python', [path.join(__dirname, '../src/run_bot.py'), url]);

  runBot.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  runBot.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  runBot.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    if (code === 0) {
      console.log(`Reading temp file from ${TEMP_FILE}`);
      fs.readFile(TEMP_FILE, 'utf8', (err, data) => {
        if (err) {
          console.error(`Error reading temp file: ${err}`);
          return res.status(500).json({ error: 'Failed to read generated tweets' });
        }
        try {
          const tweets = JSON.parse(data);
          console.log(`Parsed tweets: ${JSON.stringify(tweets, null, 2)}`);
          res.json(tweets);
        } catch (e) {
          console.error(`Error parsing temp file: ${e}`);
          res.status(500).json({ error: 'Failed to parse generated tweets' });
        }
      });
    } else {
      res.status(500).json({ error: 'Failed to generate tweets' });
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
