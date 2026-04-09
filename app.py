from visualize import create_bar, create_grouped_bar, create_radar
from compare import compare_models
import pandas as pd
import streamlit as st

input_csv = r'C:\Users\lucas\Downloads\Code\LLM Comparison\data.csv'
compare_df = pd.read_csv(input_csv)



#get list of all the LLM names
name_list = []
for name in compare_df['name']:
    name_list.append(name)

#title the app
st.title("LLM Comparison Tool")

st.caption("This is a tool to compare the pricing and capabilities of different LLMs. Select two models from the dropdowns below and click the 'Compare Models' button to see the results.")
#create two dropdowns to select models
model1 = st.selectbox("First Model", name_list)
model2 = st.selectbox("Second Model", name_list)
#creates a button to initiate the comparison of the two models
initiate = st.button("Compare Models")

#if button is pressed, run the comparison script
if initiate == True:
    #all the charts n shit
    compare_data = compare_models(model1, model2)
    st.subheader("Prompt Pricing Comparison")

    st.caption("this is a description")
    st.plotly_chart(create_bar(compare_data))
    st.subheader("Context Length and Max Completion Tokens Comparison")
    st.plotly_chart(create_grouped_bar(compare_data))
    st.subheader("Overall Comparison")
    st.plotly_chart(create_radar(compare_data))