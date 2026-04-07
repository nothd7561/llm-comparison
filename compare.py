import pandas as pd
import requests
import rapidfuzz

input_csv = r'C:\Users\lucas\Downloads\Code\LLM Comparison\data.csv'
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
    stats1 = match1[['name', 'prompt_pricing', 'completion_pricing', 'context_length', 'max_completion_tokens', 'is_moderated']]
    stats2 = match2[['name', 'prompt_pricing', 'completion_pricing', 'context_length', 'max_completion_tokens', 'is_moderated']]

    compare_data = pd.concat([stats1, stats2], axis=0)

    return compare_data