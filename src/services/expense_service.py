from config.langsmith_client import get_prompt_from_langsmith
from config.langsmith_client import get_chain


def is_expense(message):
    try:
        prompt = get_prompt_from_langsmith("expense_analysis")
        chain = get_chain(prompt)
        result = chain.invoke({"message": message})
        
        return "True" in result
    except Exception as e:
        print(f"Error when analizing message with LangChain: {e}")
        raise e

def extract_expense_category(message):
    try:
        prompt = get_prompt_from_langsmith("expense_category_extraction")
        chain = get_chain(prompt)
        result = chain.invoke({"message": message})
        
        return result
    except Exception as e:
        print(f"Error when extracting category with LangChain: {e}")
        raise e
    
def extract_expense_amount(message):
    try:
        prompt = get_prompt_from_langsmith("expense_amount_extraction")
        chain = get_chain(prompt)
        result = chain.invoke({"message": message})
        
        return result
    except Exception as e:
        print(f"Error when extracting amount with LangChain: {e}")
        raise e