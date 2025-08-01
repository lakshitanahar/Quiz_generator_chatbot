import requests

bot_name = "Quizgenerator"

# ✅ Preloaded questions
preloaded_quizzes = {
    "photosynthesis": """
Question: What is the main product of photosynthesis?
A. Oxygen
B. Carbon Dioxide
C. Glucose
D. Water

Answer: C

Question: Which pigment is responsible for photosynthesis?
A. Hemoglobin
B. Chlorophyll
C. Melanin
D. Carotene

Answer: B

Question: Which gas is absorbed during photosynthesis?
A. Oxygen
B. Nitrogen
C. Hydrogen
D. Carbon Dioxide

Answer: D
""", 
    "freedom struggle": """
Question: When did India gain independence?
A. 1945
B. 1947
C. 1950
D. 1962

Answer: B

Question: Who led the Dandi March?
A. Jawaharlal Nehru
B. Sardar Patel
C. Mahatma Gandhi
D. Bhagat Singh

Answer: C

Question: What was the name of the movement launched in 1942?
A. Quit India Movement
B. Swadeshi Movement
C. Non-Cooperation Movement
D. Civil Disobedience Movement

Answer: A
"""
    # ✅ Add more topics here 👇
    # "topic": """questions..."""
}


def get_response(user_input):
    # Convert input to lowercase to match keys
    user_input_lower = user_input.lower()

    # Check if any preloaded topic matches user input
    for topic in preloaded_quizzes:
        if topic in user_input_lower:
            return preloaded_quizzes[topic]

    # Else, use AI via LLaMA
    prompt = f"""
Generate 3 multiple-choice quiz questions based on the following topic:
"{user_input}"

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
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"⚠️ Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"🚨 Error generating quiz: {e}"
