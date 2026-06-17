from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
from langchain_core.prompts import PromptTemplate,load_prompt
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature = 0.5)
st.header("Research Input")
template = load_prompt("template.json")
paper_input = st.selectbox( "Select Research Paper Name", ["Select...", "Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] )

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )
user_input = st.text_area("Any specific instructions?")


if st.button("Summarize"):  
            chain = template | model
            result =chain.invoke({
                  'paper_input': paper_input,
                  'style_input' : style_input,
                'length_input': length_input,
               'user_input': user_input,
            })        
           
            st.write(result.content)
