from services.command_service import is_command, handle_command
from models.user_model import get_user
from services.expense_service import is_expense, extract_expense_category, extract_expense_amount
from models.expense_model import create_expense
from utils.message_response import get_message_response, get_error_message, Responses

def process_message(message_content):
    try:
        telegram_id = message_content["chatId"]
        text = message_content["text"]
        user = get_user(telegram_id)
        
        if user is None:
            if is_command(text):
                return handle_command(message_content)
        else:
            isExpense = is_expense(text)
            
            if isExpense:
                category = extract_expense_category(text)
                amount = extract_expense_amount(text)
                
                expense_data = {
                    "description": text,
                    "amount": amount,
                    "category": category,
                    "user_id": user["id"],
                    "added_at": "now()"
                }
                
                response = create_expense(expense_data)
                
                return {
                    "chat_id": telegram_id,
                    "message": get_message_response(Responses.ADDED, category)
                }

    except Exception as e:
        print(f"Error when processing message with LangChain: {e}")
        return get_error_message()