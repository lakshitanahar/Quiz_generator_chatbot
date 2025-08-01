import openai

# Set your OpenAI API Key here
openai.api_key = "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"  # replace later with your actual key

bot_name = "Quiz Generator Bot"

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
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

