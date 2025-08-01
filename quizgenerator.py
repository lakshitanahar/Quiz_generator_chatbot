import streamlit as st
import requests

bot_name = "Quiz Generator Bot"
GROQ_API_KEY = st.secrets["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"]

def get_response(topic):
    prompt = f"""
    Generate 3 multiple-choice quiz questions based on the topic: "{topic}"

    Each question should have 4 choices (A–D), one correct answer, and be clearly formatted.

    Format:
    Question: <question>
    A. <option1>
    B. <option2>
    C. <option3>
    D. <option4>
    Answer: <correct letter>
    """

    try:
        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",  # Or try llama3-70b-8192
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }
        )

        res_json = res.json()

        if res.status_code != 200:
            return f"⚠️ Error {res.status_code}: {res_json.get('error', {}).get('message', 'Unknown error')}"

        if "choices" not in res_json:
            return "⚠️ Unexpected response format. Try again later."

        return res_json["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"⚠️ Exception: {e}"
