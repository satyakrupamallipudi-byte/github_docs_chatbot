import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.title("GitHub Docs Chatbot")

with open("data/github_docs.txt", "r", encoding="utf-8") as file:
    docs = file.read()

question = st.text_input("Ask a question")

if st.button("Get Answer") and question:

    prompt = f"""
Use the documentation below to answer.

Documentation:
{docs}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    st.write(response.text)