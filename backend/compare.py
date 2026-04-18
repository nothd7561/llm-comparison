import pandas as pd
import requests
import rapidfuzz
from backend.benchmark import get_benchmark

input_csv = 'data_fetching/data.csv'
compare_df = pd.read_csv(input_csv)

def compare_models(model_1, model_2):
    #create a list of all the names in the 'name' column of the compare_df dataframe
    name_list = []
    for name in compare_df['name']:
        name_list.append(name)

    #return the best match for model_1 in the name_list using rapidfuzz
    result = rapidfuzz.process.extractOne(model_1, name_list)
    result2 = rapidfuzz.process.extractOne(model_2, name_list)

    #filters the dataframe to only include the row where the 'name' column matches the result of the fuzzy matching
    match1 = compare_df[compare_df['name'] == result[0]]
    match2 = compare_df[compare_df['name'] == result2[0]]
    #pick the columns 'prompt_pricing', 'completion_pricing', 'context_length', 'max_completion_tokens', and 'is_moderated' from the match1 and match2 dataframes
    stats1 = match1[['id','name', 'prompt_pricing', 'completion_pricing', 'context_length', 'max_completion_tokens', 'is_moderated']]
    stats2 = match2[['id','name', 'prompt_pricing', 'completion_pricing', 'context_length', 'max_completion_tokens', 'is_moderated']]

    compare_data = pd.concat([stats1, stats2], axis=0)
    compare_data = compare_data.rename(columns={'name': 'Model Name',
                                                'prompt_pricing': 'Prompt Pricing (Tokens)', 
                                                'completion_pricing': 'Completion Pricing (Tokens)',
                                                'context_length': 'Context Length',
                                                'max_completion_tokens': 'Max Completion Tokens',
                                                'is_moderated': 'Moderated'
                                                })
    
    bench1 = get_benchmark(model_1)
    bench2 = get_benchmark(model_2)
    compare_data["Intel Index"] = bench1[0], bench2[0]
    compare_data["Code Index"] = bench1[1], bench2[1]
    compare_data["Math Index"] = bench1[2], bench2[2]
    compare_data["Latency"] = bench1[3], bench2[3]
    compare_data["Output Speed"] = bench1[4], bench2[4]
    return compare_data


print(compare_models("GPT 4.1", "Claude Opus"))