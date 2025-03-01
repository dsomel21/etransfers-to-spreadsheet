# AI Agent Experiments

An experimental project exploring the development of practical and reusable AI agents using browser-use and LangChain.

This AI agent will get all e-transfers from your **email** and put them into a new Google Spreadsheet on your Google account (using your browser).

| Time + Date            | Amount          | Name           | Email                      | Description        | Reference Number | Status                                          |
|------------------------|-----------------|----------------|----------------------------|--------------------|------------------|-------------------------------------------------|
| Mar 1, 2025, 4:45 PM  | $825.00 (USD)   | Robert Walker  | robert.walker@example.ca | Yu-Gi-Oh cards | AB12CD34EFGH     | Deposited (into BMO account ending in 1234)     |


See _Engineering Notes_ and _Final Thoughts_ for more info.

<img width="915" alt="Data scraping" src="https://github.com/user-attachments/assets/ac2bcdf4-fb71-49ca-b446-5dc4345e148a" />

## Overview

This project leverages [browser-use](https://github.com/browser-use/browser-use) to create AI agents capable of automating browser-based tasks. Unlike traditional automation that uses isolated Chromium instances, this implementation deliberately uses your local Chrome installation to maintain authentication states and access existing user profiles.

## Setup

### 1. Install dependencies:

You will need `browser-use`

```bash
pip install browser-use langchain-anthropic python-dotenv
```

and you will need `playwright`:

```bash
npm install -g playwright

playwright install
```

### 2. Configure environment variables in `.env`:

```
ANTHROPIC_API_KEY=your_key_here
```

### 3. Run the agent:

```bash
python gmail_transfer_checker.py
```

## Technical Details

This implementation uses a real Chrome browser instance instead of Playwright's bundled Chromium. For detailed configuration options, see the [browser-use Real Browser documentation](https://docs.browser-use.com/customize/real-browser).

## Engineering Notes

Performance considerations:

- CPU utilization is significant during agent operation due to concurrent LLM inference and browser automation
- Extended runtime expectations: Tasks involving multiple browser interactions can take +10 minutes to complete due to LLM thinking time and browser state management
- Thermal management may be necessary during extended operations, especially on laptops

## Final Thoughts

The AI agent’s repetitive steps are inefficient, as it retries each action rather than optimizing the sequence. This causes lengthy run times.

Honestly... a more effective strategy would involve creating web scrapers to handle routine DOM-based tasks and reserving AI for tasks like summarizing or handling unexpected logic. 🤷🏽‍♂️

## License

MIT
