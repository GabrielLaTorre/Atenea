import os
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOpenAI
from config.langsmith_client import get_prompt_from_langsmith
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.2
)

def is_expense(message):
    """Analiza un mensaje usando LangChain y LangSmith."""
    print("Analyzing message with LangChain..", message)
    try:
        prompt = get_prompt_from_langsmith("expense_analysis")
        expense_chain = prompt | llm | StrOutputParser()
        result = expense_chain.invoke({"message": message})
        
        print('result', result)
        return "True" in result
    except Exception as e:
        print(f"Error when analizing message with LangChain: {e}")
        return False
