import plotly.express as px
#from compare import compare_models
import plotly.graph_objects as go

#calls the comparison script on the two models and stores the result in a variable called compare_data
#compare_data = compare_models(model1, model2)

def create_bar(data):
    #creates a bar chart using plotly express to compare the prompt pricing of the two models
    bar_chart = px.bar(data, 
                                x='Model Name', 
                                y='Prompt Pricing (Tokens)',
                                barmode='group')
    bar_chart.update_layout(
        yaxis = dict(
            range=[0, .00015]
        )
    )
    return bar_chart


def create_bar_length(data):
    #creates a bar chart using plotly express to compare the context length of the two models
    bar_chart = px.bar(data, 
                                x='Model Name', 
                                y='Context Length',
                                barmode='group')
    bar_chart.update_layout(
        yaxis = dict(
            range=[0, 2000000]))
    return bar_chart

def create_bar_tokens(data):
    #creates a bar chart using plotly express to compare the max completion tokens of the two models
    bar_chart = px.bar(data, 
                                x='Model Name', 
                                y='Max Completion Tokens',
                                barmode='group')
    bar_chart.update_layout(
        yaxis = dict(
            range=[0, 1000192]))
    return bar_chart

#def create_grouped_bar(data):
    #creates a grouped bar chart using plotly express to compare the context length and max completion tokens of the two models
    melt_data = data.melt(id_vars=['Model Name'], value_vars=['Context Length', 'Max Completion Tokens'], var_name='Metrics', value_name='Amount(Tokens)')
    grouped_bar_chart = px.bar(melt_data, 
                                  x='Metrics', 
                                  y='Amount(Tokens)',
                                  color='Model Name',
                                  barmode='group')
    return grouped_bar_chart
 
#creates a radar chart using plotly graph objects to compare the context length, max completion tokens, prompt pricing, and completion pricing of the two models
def create_radar(data):

    #normalize the context length, max completion tokens, prompt pricing, and completion pricing values for the two models to be between 0 and 1
    norm_length1 = data['Context Length'].values[0] / data['Context Length'].max()
    norm_tokens1 = data['Max Completion Tokens'].values[0] / data['Max Completion Tokens'].max()
    norm_length2 = data['Context Length'].values[1] / data['Context Length'].max()
    norm_tokens2 = data['Max Completion Tokens'].values[1] / data['Max Completion Tokens'].max()
    norm_pricing1 = data['Prompt Pricing (Tokens)'].values[0] / data['Prompt Pricing (Tokens)'].max()
    norm_pricing2 = data['Prompt Pricing (Tokens)'].values[1] / data['Prompt Pricing (Tokens)'].max()
    norm_completion1 = data['Completion Pricing (Tokens)'].values[0] / data['Completion Pricing (Tokens)'].max()
    norm_completion2 = data['Completion Pricing (Tokens)'].values[1] / data['Completion Pricing (Tokens)'].max()

#radar chart to compare the two models
    radar_chart = go.Figure()
    radar_chart.add_trace(go.Scatterpolar(
        r=[norm_length1, norm_tokens1, norm_pricing1, norm_completion1],
        theta=['Context Length', 'Max Completion Tokens', 'Prompt Pricing (Tokens)', 'Completion Pricing (Tokens)'],
        name=data['Model Name'].values[0],
        fill='toself'
    ))#uwu
    radar_chart.add_trace(go.Scatterpolar(
        r=[norm_length2, norm_tokens2, norm_pricing2, norm_completion2],
        theta=['Context Length', 'Max Completion Tokens', 'Prompt Pricing (Tokens)', 'Completion Pricing (Tokens)'],
        name=data['Model Name'].values[1],
        fill='toself'
    ))
    
    radar_chart.update_layout(
        polar=dict(
            radialaxis=dict(
                tickfont=dict(color='black')
            )
        )
    )


    return radar_chart


def create_benchmark_bar(data):
    data_melt = data.melt(
        id_vars='Model Name',
        value_vars=['Intel Index', 'Code Index', 'Math Index'],
        var_name='Metrics',
        value_name='Score'
    )
    grouped_bar = px.bar(data_melt, x='Metrics', y='Score', color='Model Name', barmode='group')
    grouped_bar.update_layout(
        yaxis = dict(
            range=[0, 70]))
    return grouped_bar

#calls the create_bar, create_grouped_bar, and create_radar functions on the compare_data variable and shows the resulting charts

  