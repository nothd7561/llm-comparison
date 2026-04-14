
# NOTE: This script was an attempt to pull real-time latency data for each model
# using the OpenRouter /endpoints API. It was ultimately scrapped because most models
# don't have latency data available — too many returned None to be useful as a metric.
# Keeping this as a reference for the caching pattern and API exploration process.

import pandas as pd
import requests
from pathlib import Path


# hits the OpenRouter endpoints API for a given model and returns average latency across all providers
# the /endpoints route returns one entry per provider serving that model
def pull_latency(model_id):
    URL = f'https://openrouter.ai/api/v1/models/{model_id}/endpoints'
    response = requests.get(URL)
    print(response.status_code)
    data_json = response.json()
    latency = data_json['data']['endpoints']

    # loop through each provider and collect their latency values
    # skip None values — many providers don't report latency
    latency_values = []
    for endpoint in latency:
        if endpoint['latency_last_30m'] is not None:
            latency_values.append(endpoint['latency_last_30m'])

    # return the average if we have values, otherwise return None
    if len(latency_values) != 0:
        avg_latency = sum(latency_values) / len(latency_values)
        return avg_latency
    if len(latency_values) == 0:
        return None


# path to the local cache file
file_path = Path("C:\\Users\\lucas\\Downloads\\Code\\LLM Comparison\\latency.csv")

# load existing cache if it exists, otherwise create an empty one
if file_path.exists() == True:
    latency_df = pd.read_csv(file_path)
else:
    latency_df = pd.DataFrame(columns=['id', 'average_latency'])


# checks the cache before calling the API — avoids redundant requests for already-fetched models
def get_latency(model_id):
    global latency_df
    if model_id in latency_df['id'].values:
        return latency_df[latency_df['id'] == model_id]['average_latency'].values[0]
    else:
        latency_value = pull_latency(model_id)
        new_row = {'id': model_id, 'average_latency': latency_value}
        latency_df = pd.concat([latency_df, pd.DataFrame([new_row])], ignore_index=True)
        latency_df.to_csv(file_path, index=False)
        return latency_value


print(get_latency("anthropic/claude-sonnet-4.6"))
    




