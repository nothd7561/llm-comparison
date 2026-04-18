import pandas as pd
import requests
import json
import rapidfuzz

#load the json file "cache.json" into a variable called data_json
with open("cache.json") as f:
    data_json = json.load(f)


def get_benchmark(model_name):
    #create a list of all the AI model names
    name_list = []
    for model in data_json['data']:
        name_list.append(model['name'])
    #use rapidfuzz to find the best match for the model_name in the name_list
    best_match = rapidfuzz.process.extractOne(model_name, name_list)[0]

    #for each model in the data_json['data'] list, if the model's name matches the best_match,  
    #return the values of the 'artificial_analysis_intelligence_index', 'artificial_analysis_coding_index', and 'artificial_analysis_math_index' keys from the 'evaluations' dictionary
    for model in data_json['data']:
        if model['name'] == best_match:
            intel_index = model['evaluations']['artificial_analysis_intelligence_index']
            code_index = model['evaluations']['artificial_analysis_coding_index']
            math_index = model['evaluations']['artificial_analysis_math_index']
            response_latency = model['median_time_to_first_token_seconds']
            output_speed = model['median_output_tokens_per_second']
            return intel_index, code_index, math_index, response_latency, output_speed

print(get_benchmark("GPT 4.1"))








