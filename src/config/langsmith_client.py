import os
from dotenv import load_dotenv
from langsmith import Client
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.2
)

client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))

def get_prompt_from_langsmith(prompt_key: str) -> str:
    try:
        prompt = client.pull_prompt(prompt_key)
        return prompt
    except Exception as e:
        print(f"❌ Error in LangSmith: {e}")

def get_chain(prompt):
    return prompt | llm | StrOutputParser()