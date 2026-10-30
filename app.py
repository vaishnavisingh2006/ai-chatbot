import streamlit as st 

st.header("College Chatbot")
st.subheader("Ask me anything...")
prompt = st.text_area("Enter your Question!")
btn = st.button("Ask")

from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model(
    "google_genai:gemini-3.5-flash-lite",
)

if btn:
    response = model.invoke(prompt)
    st.write(response.text)

    
    