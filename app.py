from visualize import create_bar, create_grouped_bar, create_radar
from compare import compare_models
import pandas as pd
import streamlit as st

input_csv = r'C:\Users\lucas\Downloads\Code\LLM Comparison\data.csv'
compare_df = pd.read_csv(input_csv)

name_list = []
for name in compare_df['name']:
    name_list.append(name)

st.title("LLM Comparison Tool")
model1 = st.selectbox("First Model", name_list)
model2 = st.selectbox("Second Model", name_list)
initiate = st.button("Compare Models")
if initiate == True:
    compare_data = compare_models(model1, model2)
    st.subheader("Prompt Pricing Comparison")
    st.plotly_chart(create_bar(compare_data))
    st.subheader("Context Length and Max Completion Tokens Comparison")
    st.plotly_chart(create_grouped_bar(compare_data))
    st.subheader("Overall Comparison")
    st.plotly_chart(create_radar(compare_data))