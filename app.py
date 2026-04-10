from visualize import create_bar, create_bar_length, create_bar_tokens, create_radar
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

#graph explanation for prompt pricing
    st.caption("This chart compares the prompt pricing of the two models. The lower the prompt pricing, the cheaper it is to use the model for generating text. AKA: The lower the bar, the better.")
    st.caption("Note: The y-axis is limited to .00015 to better visualize the differences between the two models. ")
    st.caption("The greek symbol is mew, which is by the millionth. Multiply the coefficients by .000001 to get the actual price per token.")
    st.plotly_chart(create_bar(compare_data))

    st.subheader("Context Length Comparison")
    st.caption("Context length is the total number of tokens (words) the model can process at one time.")
    st.caption("The size of the workspace the AI has on it's desk.")
    st.caption("The higher the context length, the more information the model can retain.")
    st.plotly_chart(create_bar_length(compare_data))

    st.subheader("Max Completion Tokens Comparison")
    st.caption("Max completion tokens is the maximum length of the AI's response.")
    st.caption("The higher the max completion tokens, the more text the model can generate.")
    st.plotly_chart(create_bar_tokens(compare_data))

    st.subheader("Overall Comparison")
    st.plotly_chart(create_radar(compare_data))