import pandas as pd
import requests
from dotenv import load_dotenv
import os
import json

cache = ("cache.json")

#checks if cache file exists
if os.path.exists(cache):
    #if it exists, load the data from the cache and call it f
    with open(cache) as f:
        #load the json data from the cache into a variable called data_json
        data_json = json.load(f)
else: 
    #if cache file doesn't exist, pull from API and create it
    load_dotenv(r'C:\Users\lucas\Downloads\Code\LLM Comparison\.env')
    api_key = os.getenv("API_KEY2")

    response = requests.get(
        "https://artificialanalysis.ai/api/v2/data/llms/models",
        headers={"x-api-key": api_key},
    )
    data_json = response.json()
    print(response.status_code)
    #load the json data from the API into data_json 
    with open(cache, "w") as f:
        #save the json data into the cache file
        #saves a dictionary/JSON to a JSON file
        json.dump(data_json, f)








#475 models
    

    