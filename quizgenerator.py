import os
import openai

# Bot Name
bot_name = "Quiz Generator Bot"

# Set your API key (make sure it's set in your Streamlit Secrets or env variable in real deploy)
openai.api_key = os.getenv("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")  # or you can hardcode temporarily for testing

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
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"
