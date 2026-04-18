# LLM Comparison Tool

A Streamlit web app for comparing AI language models side by side on pricing, performance, and benchmark scores.

---

## What it does

Select any two models from 400+ LLMs and compare them on:

- **Response Latency** — how fast the model starts responding
- **Output Speed** — tokens generated per second
- **Intelligence, Code, and Math Index** — benchmark scores from Artificial Analysis
- **Prompt Pricing** — cost per input token
- **Context Length** — how much information the model can hold in memory
- **Max Completion Tokens** — maximum length of the model's response

---

## Data Sources

- [OpenRouter](https://openrouter.ai) — pricing, context length, token limits
- [Artificial Analysis](https://artificialanalysis.ai) — benchmark scores, latency, output speed

---

## Stack

- Python, Streamlit, Plotly, pandas, rapidfuzz

---

## Setup

1. Clone the repo
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Run `streamlit run tool.py` to start the app

---

## Author

Lucas Lu — ll207@rice.edu — [LinkedIn](https://www.linkedin.com/in/lucas-lu6978)


