"""
Simple script that runs the task of opening amazon and searching.
@dev Ensure we have a `ANTHROPIC_API_KEY` variable in our `.env` file.
"""

import os
import sys
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

# Load environment variables from .env file
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from browser_use import Agent, Browser, BrowserConfig
import time  # Add this import at the top

llm = ChatAnthropic(model_name='claude-3-7-sonnet-20250219', temperature=0.0, timeout=3, stop=None)

# Configure to use your actual Chrome browser
browser = Browser(
	config=BrowserConfig(
		chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # for macOS
	)
)

task= """
0. We need an array where we will be storing some objects that will have the following information: 'Time+Date', 'Amount', 'Name', 'Email', 'Description', 'Reference Number', 'Status'
1. Go to https://mail.google.com/mail/u/0/#search/Interac+e-transfer+you've+received. Keep this tab open at all times.
2. Go through each result that looks like a cash transfer and right click on the email and click "Open in new window". 
3. Get the information from the email and put it into the array.
4. Once that information is added to our array, we can close the email window.
5. We can then go to the next email result that looks like an cash transfer and repeat the process.
6. Once we have reached the bottom of the email results, we must check if there is a next page of results. To go to the next page, you can do "/p2" at the end of the URL. For example, "https://mail.google.com/mail/u/0/#search/Interac+e-transfer+you've+received/p2" will take you to the second page of results. p3 will take you to the third page of results, and so on.
7. If there is a next page of results, we can go to the next page and repeat the process.
8. Continue until we have reached the end of the email results or until we have gotten all emails after 2024.
9. Finally, I need you to put all this information into a new Google Sheet and print out the array
"""

agent = Agent(
	task=task,
	llm=llm,
	browser=browser,
)

async def main():
	start_time = time.time()
	print(f"Starting task at {time.strftime('%H:%M:%S')}")
	
	await agent.run(max_steps=300)
	
	end_time = time.time()
	duration = end_time - start_time
	print(f"\nTask completed at {time.strftime('%H:%M:%S')}")
	print(f"Total execution time: {duration:.2f} seconds ({duration/60:.2f} minutes)")
	
	input('Press Enter to close the browser...')
	await browser.close()

asyncio.run(main())
