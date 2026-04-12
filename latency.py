import pandas as pd
import requests
from pathlib import Path

URL = f"https://openrouter.ai/api/v1/models/google/gemma-4-26b-a4b-it/endpoints"
response = requests.get(URL)
print(response.json()['data']['endpoints'])


def pull_latency(model_id):
    URL = f'https://openrouter.ai/api/v1/models/{model_id}/endpoints'
    response = requests.get(URL)
    data_json = response.json()
    latency = data_json['data']['endpoints']
    return latency['latency_last_30m']


file_path = Path("C:\\Users\\lucas\\Downloads\\Code\\LLM Comparison\\latency.csv")

def get_latency(model_id):
    if model_id in cache['id']:
        return cache['id']

if file_path.exists() == True:
    cache = pd.read_csv(file_path)


else:
    cache = pd.DataFrame(columns=['id','latency'])
    cache.to_csv(file_path, index=False)
