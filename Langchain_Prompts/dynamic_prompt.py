from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

st.header('Research Tool')

paper_input = st.selectbox("Select Research paper name", [ "Ai" , "SDE", "Gen Ai"]);
style_input = st.selectbox("Select explanation style:", ["beginner freindly", "maths heavy", "codeheavy"])
length_input = st.selectbox("Select Lengt", ["1 line", "2line", "3 line"]);
# template = PromptTemplate(
#     template=""" 
#     Summarize this paper titled"{paper_input} in a style "{style_input}" which has length
#     of"{length_input}"
    
#     """,
#     input_variables=['paper_input', 'style_input', 'length_input'],
#     validate_template = True
    
# )

template = load_prompt('template.json')



# fill the placeholders
# prompt = template.invoke({
#     'paper_input' : paper_input,
#     'style_input' : style_input, 
#     'length_input': length_input
# })




# if st.button('Summarize'): 
#     result = model.invoke(prompt)
#     st.write(result.content)


if st.button('Summarize'):
    chain = template | model
    result =  chain.invoke({
        'paper_input' : paper_input,
        'style_input' : style_input, 
        'length_input': length_input
        }) 
    
    st.write(result.content)



    
    