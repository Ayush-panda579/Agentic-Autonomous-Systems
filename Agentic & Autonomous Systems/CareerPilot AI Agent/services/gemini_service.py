import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("AQ.Ab8RN6JUzOLty5mFtEaBgEtOxM-haG_Rhbk6iZaR_YQR9oBGyQ")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_ai_response(prompt):

    response = model.generate_content(prompt)

    return response.text