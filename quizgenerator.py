import os
import requests

# Bot Name
bot_name = "Quiz Generator Bot"

# Your Groq API Key
GROQ_API_KEY = os.getenv("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")  # Will read from Streamlit secrets

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
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",  # You can also try "llama3-70b-8192"
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }
        )
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"⚠️ Error: {e}"
