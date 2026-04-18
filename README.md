# LLM-Comparison

A Streamlit web app for comparing AI language models side by side on pricing, performance, and benchmark scores.

What it does
Select any two models from 400+ LLMs and compare them on:

Response Latency — how fast the model starts responding
Output Speed — tokens generated per second
Intelligence, Code, and Math Index — benchmark scores from Artificial Analysis
Prompt Pricing — cost per input token
Context Length — how much information the model can hold in memory
Max Completion Tokens — maximum length of the model's response
Data Sources
OpenRouter — pricing, context length, token limits
Artificial Analysis — benchmark scores, latency, output speed
Stack
Python, Streamlit, Plotly, pandas, rapidfuzz
Setup
Clone the repo
Install dependencies: pip install -r requirements.txt
Add a .env file with your API keys:

API_KEY=your_openrouter_key
API_KEY2=your_artificial_analysis_key
Run python data_fetching/fetch.py to pull model data
Run streamlit run tool.py to start the app
Author
Lucas Lu — ll207@rice.edu — LinkedIn
