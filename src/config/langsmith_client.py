import os
from langsmith import Client
from dotenv import load_dotenv

load_dotenv()

client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))

def get_prompt_from_langsmith(prompt_key: str) -> str:
    try:
        prompt = client.pull_prompt(prompt_key)
        print('prompt', prompt)
        return prompt
    except Exception as e:
        print(f"❌ Error in LangSmith: {e}")
