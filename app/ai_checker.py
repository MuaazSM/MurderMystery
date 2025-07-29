import os
from langchain_google_genai import ChatGoogleGenerativeAI
from app.prompt_templates import build_prompt

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    temperature = "0.8"
)

def evaluate(mystery, user_input):
    prompt = build_prompt(mystery, user_input)
    response = llm.invoke(prompt)
    return response.strip()