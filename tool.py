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
st.subheader("1 Token = .75 words/4 characters")


#create two dropdowns to select models
model1 = st.sidebar.selectbox("Model 1", name_list)
model2 = st.sidebar.selectbox("Model 2", name_list)
st.sidebar.markdown("First Project, Don't Flame me!")
st.sidebar.markdown("General Idea: Compare two LLMs on various metrics.")
st.sidebar.markdown("Data Attrition: Openrouter AI, Artificial Analysis")
st.sidebar.markdown("Gmail: ll207@rice.edu")
st.sidebar.markdown("LinkedIn: www.linkedin.com/in/lucas-lu6978")
st.sidebar.markdown("Github: https://github.com/nothd7561/llm-comparison")
                    
#creates a button to initiate the comparison of the two models
initiate = st.button("Compare")

#if button is pressed, run the comparison script
if initiate == True:
    #all the charts n shit
    compare_data = compare_models(model1, model2)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(compare_data["Model Name"].values[0])
        st.metric(label="Response Latency (Seconds)", value=compare_data["Latency"].values[0])
        st.metric(label="Output Speed (Tokens/Second)", value=compare_data["Output Speed"].values[0])
    with col2:
        st.subheader(compare_data["Model Name"].values[1])
        st.metric(label="Response Latency (Seconds)", value=compare_data["Latency"].values[1])
        st.metric(label="Output Speed (Tokens/Second)", value=compare_data["Output Speed"].values[1])
    st.subheader("Model Index Scores")
    st.caption("Attritioned from Artificial Analysis")
    st.caption("Intel Index measures general reasoning, problem solving ability, and logic.")
    st.caption("Code Index measures how well the LLM can write code, debug, and understand languages.")
    st.caption("Math Index measures mathmematical reasoning ability. Proofs, world problems, etc. ")
    st.plotly_chart(create_benchmark_bar(compare_data))

    st.subheader("Prompt Pricing")
    st.caption("Prompt Pricing is how much you're charged for sending an input.")
    st.caption("Higher Number = More expensive.")
    st.plotly_chart(create_bar(compare_data))

    st.subheader("Max Completion Tokens")
    st.caption("Max Completion Tokens is the maximum length of the AI's answer.")
    st.plotly_chart(create_bar_tokens(compare_data))

    st.subheader("Context Length")
    st.caption("Context Length is the amount of information the model can remember in your chat.")
    st.caption("This includes pasted documents, input messages, files, earlier chat history, etc.")
    st.caption("Higher = Better")
    st.plotly_chart(create_bar_length(compare_data))

    st.subheader("Overall Rating")
    st.plotly_chart(create_radar(compare_data))
