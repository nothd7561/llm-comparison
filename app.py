from backend.visualize import create_bar, create_bar_length, create_bar_tokens, create_radar, create_benchmark_bar
from backend.compare import compare_models
import pandas as pd
import streamlit as st

input_csv = r'C:\Users\lucas\Downloads\Code\LLM Comparison\data_fetching\data.csv'
compare_df = pd.read_csv(input_csv)



#get list of all the LLM names
name_list = []
for name in compare_df['name']:
    name_list.append(name)

#title the app
st.title("AI Model Comparison Sideproject")


#create two dropdowns to select models
model1 = st.sidebar.selectbox("Model 1", name_list)
model2 = st.sidebar.selectbox("Model 2", name_list)
st.sidebar.markdown("First Project, Don't Flame me!")
st.sidebar.markdown("General Idea: Compare two LLMs on various metrics.")
st.sidebar.markdown("Data Attrition: Openrouter AI, Artificial Analysis")
st.sidebar.markdown("Gmail: ll207@rice.edu")
st.sidebar.markdown("LinkedIn: www.linkedin.com/in/lucas-lu6978")
st.sidebar.markdown("Documentation and Github will come later!")
                    
#creates a button to initiate the comparison of the two models
initiate = st.button("Compare")

#if button is pressed, run the comparison script
if initiate == True:
    #all the charts n shit
    compare_data = compare_models(model1, model2)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Response Latency (Seconds)", value=compare_data["Latency"].values[0])
        st.metric(label="Output Speed (Tokens/Second)", value=compare_data["Output Speed"].values[0])
    with col2:
        st.metric(label="Response Latency (Seconds)", value=compare_data["Latency"].values[1])
        st.metric(label="Output Speed (Tokens/Second)", value=compare_data["Output Speed"].values[1])
    
    st.plotly_chart(create_benchmark_bar(compare_data))
    st.plotly_chart(create_bar(compare_data))
    st.plotly_chart(create_bar_tokens(compare_data))
    st.plotly_chart(create_bar_length(compare_data))
    st.plotly_chart(create_radar(compare_data))
