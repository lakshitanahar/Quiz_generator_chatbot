import streamlit as st
from quizgenerator import get_response, bot_name

st.set_page_config(page_title="Quiz Generator", layout="centered")
st.title(f"📚 {bot_name}")
st.write("Enter a topic to generate multiple-choice questions using AI.")

topic = st.text_input("Enter a Topic", placeholder="e.g. Python Basics")

if st.button("Generate Quiz"):
    if topic:
        with st.spinner("Generating questions..."):
            quiz = get_response(topic)
            st.success("Here are your questions:")
            st.text_area("Quiz", quiz, height=300)
    else:
        st.warning("Please enter a topic first.")
