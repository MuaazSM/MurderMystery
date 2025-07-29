import os
from langchain_google_genai import ChatGoogleGenerativeAI
from app.prompt_templates import build_prompt
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    temperature = "0.8",
    google_api_key=GEMINI_API_KEY
)

def evaluate(mystery, user_input):
    prompt = build_prompt(mystery, user_input)
    response = llm.invoke(prompt)
    return response.strip()