import gradio as gr
import ollama

# Function to process user queries
def solve_math_problem(problem):
	response = ollama.chat(model='deepscaler', messages=[{'role': 'user', 'content': problem}])
	return response['message']

# Define Gradio Interface
interface = gr.Interface(
	fn = solve_math_problem,
	inputs = gr.Textbox(label="Enter a math problem"),
	outputs = gr.Textbox(label="Solution"),
	title = "AI-Powered Math Solver",
	description = "Ask any math question, and Deepscaler will provide a step-by-step solution."
)

# Launch the App
interface.launch()