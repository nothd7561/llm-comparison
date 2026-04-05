import pandas as pd
import requests

import_csv = r'C:\Users\lucas\Downloads\Code\LLM Comparison\data.csv'
compare_df = pd.read_csv(import_csv)



def separate(dict):
    for key, value in dict.items():
        value1 = dict[key]

user_model = input("First Model:  ")
for index, row in compare_df.iterrows():
    if row['name'] == user_model:
        model1 = row[['name', 'created', 'context_length', 'pricing', 'top_provider']]
        

        
user_model2 = input("Second Model:  ")
for index, row in compare_df.iterrows():
    if row['name'] == user_model2:
        model2 = row[['name', 'created', 'context_length', 'pricing', 'top_provider']]

comparison_df = pd.concat([model1, model2], axis=0)