import pandas as pd
import requests
import json
import rapidfuzz

with open("cache.json") as f:
    data_json = json.load(f)


def get_benchmark(model_name):
    name_list = []
    for model in data_json['data']:
        name_list.append(model['name'])

    best_match = rapidfuzz.process.extractOne(model_name, name_list)[0]
    for model in data_json['data']:
        if model['name'] == best_match:
            intel_index = model['evaluations']['artificial_analysis_intelligence_index']
            code_index = model['evaluations']['artificial_analysis_coding_index']
            math_index = model['evaluations']['artificial_analysis_math_index']
            return intel_index, code_index, math_index
        
print(get_benchmark("GPT 4"))








