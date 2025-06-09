import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def evaluate_answer(user_answer, style_instruction="Provide a thorough and detailed analysis."):
    prompt = f"""
You are an expert interview coach.

Here is a candidate's answer to a behavioral interview question:
"{user_answer}"

Evaluate the response on:
- Clarity (1-5)
- STAR format use (1-5)
- Impactfulness (1-5)

{style_instruction}

Then provide short, actionable feedback on how to improve.
"""
    response = model.generate_content(prompt)
    return response.text