import streamlit as st
from quizgenerator import get_response, bot_name

# Set Streamlit page config
st.set_page_config(page_title="AI Quiz Generator", layout="centered")

# UI elements
st.title("🧠 AI Quiz Generator Chatbot")
st.write("Generate multiple-choice quiz questions based on any topic using LLaMA3 (Groq API)")

# Input from user
topic = st.text_input("📘 Enter a topic to generate quiz questions", placeholder="e.g. Python Functions")

if st.button("Generate Quiz"):
    if topic.strip() == "":
        st.warning("Please enter a topic to generate quiz.")
    else:
        with st.spinner("Generating quiz..."):
            quiz = get_response(topic)
            st.success("Here’s your quiz:")
            st.text_area("📋 Quiz Output", quiz, height=300)

