import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()

print("\n🔍 Available Models:\n")
for m in models:
    print(f"- {m.name}")