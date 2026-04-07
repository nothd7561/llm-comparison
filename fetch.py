import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv(r'C:\Users\lucas\Downloads\Code\LLM Comparison\.env')
api_key = os.getenv("API_KEY")

URL = "https://openrouter.ai/api/v1/models"

response = requests.get(URL, headers =
                        {'Authorization': f'Bearer {api_key}',}
                        )

data_json = response.json()
data_df = pd.DataFrame(data_json['data'])

#prompt function to extract prompt pricing from the 'pricing' column
def get_prompt(df):
    return df['pricing']['prompt']

#completion function to extract completion pricing from the 'pricing' column
def get_completion(df):
    return df['pricing']['completion']

#functions to extract context length, max tokens, and moderated from the 'top_provider' column
def get_context_length(df):
    return df['top_provider']['context_length']
def get_max_tokens(df):
    return df['top_provider']['max_completion_tokens']
def get_moderated(df):
    return df['top_provider']['is_moderated']

#createw new columns for prompt and completion pricing
data_df['prompt_pricing'] = data_df.apply(get_prompt, axis=1)
data_df['completion_pricing'] = data_df.apply(get_completion, axis=1)

#create new columns for context length, max tokens, and moderated
data_df['context_length'] = data_df.apply(get_context_length, axis=1)
data_df['max_completion_tokens'] = data_df.apply(get_max_tokens, axis=1)
data_df['is_moderated'] = data_df.apply(get_moderated, axis=1)

data_df = data_df.drop(columns=['pricing', 'top_provider'])

data_df.to_csv(r'C:\Users\lucas\Downloads\Code\LLM Comparison\data.csv', index=False)