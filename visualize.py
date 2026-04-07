import plotly.express as px
from compare import compare_models
import plotly.graph_objects as go

#prompts the user for the two models they want to compare
model1 = input("First Model: ")
model2 = input("Second Model: ")

#calls the comparison script on the two models and stores the result in a variable called compare_data
compare_data = compare_models(model1, model2)



def create_bar(data):
    #creates a bar chart using plotly express to compare the prompt pricing of the two models
    bar_chart = px.bar(data, 
                                x='name', 
                                y='prompt_pricing',
                                barmode='group')
    return bar_chart

def create_grouped_bar(data):
    #creates a grouped bar chart using plotly express to compare the context length and max completion tokens of the two models
    melt_data = data.melt(id_vars=['name'], value_vars=['context_length', 'max_completion_tokens'], var_name='metric', value_name='value')
    grouped_bar_chart = px.bar(melt_data, 
                                  x='metric', 
                                  y='value',
                                  color='name',
                                  barmode='group')
    return grouped_bar_chart

def create_radar(data):

    norm_length1 = data['context_length'].values[0] / data['context_length'].max()
    norm_tokens1 = data['max_completion_tokens'].values[0] / data['max_completion_tokens'].max()
    norm_length2 = data['context_length'].values[1] / data['context_length'].max()
    norm_tokens2 = data['max_completion_tokens'].values[1] / data['max_completion_tokens'].max()
    norm_pricing1 = data['prompt_pricing'].values[0] / data['prompt_pricing'].max()
    norm_pricing2 = data['prompt_pricing'].values[1] / data['prompt_pricing'].max()
    norm_completion1 = data['completion_pricing'].values[0] / data['completion_pricing'].max()
    norm_completion2 = data['completion_pricing'].values[1] / data['completion_pricing'].max()


    radar_chart = go.Figure()
    radar_chart.add_trace(go.Scatterpolar(
        r=[norm_length1, norm_tokens1, norm_pricing1, norm_completion1],
        theta=['context_length', 'max_completion_tokens', 'prompt_pricing', 'completion_pricing'],
        name='Model 1',
        fill='toself'
    ))
    radar_chart.add_trace(go.Scatterpolar(
        r=[norm_length2, norm_tokens2, norm_pricing2, norm_completion2],
        theta=['context_length', 'max_completion_tokens', 'prompt_pricing', 'completion_pricing'],
        name='Model 2',
        fill='toself'
    ))
    return radar_chart

bar_show = create_bar(compare_data)
grouped_bar_show = create_grouped_bar(compare_data)
radar_show = create_radar(compare_data)
bar_show.show()
grouped_bar_show.show() 
radar_show.show()   
  