import gradio as gr

def generate_quiz(topic):
    # Your logic here — this is just an example
    return f"""🧠 Quiz on "{topic}"
    
1. What is {topic}?
2. Why is {topic} important?
3. Name a real-world use of {topic}.
4. Explain {topic} in simple words.
"""

iface = gr.Interface(
    fn=generate_quiz,
    inputs=gr.Textbox(lines=1, placeholder="Enter quiz topic..."),
    outputs="text",
    title="📚 QuizGenerator Bot",
    description="Type a topic and generate an instant quiz!"
)

iface.launch()
