from services.command_service import is_command, handle_command
from models.user_model import get_user
from services.expense_service import is_expense

def process_message(message_content):
    """Procesa el mensaje con LangChain y lo guarda en Supabase si es un gasto."""
    
    try:
        telegram_id = message_content["chatId"]
        text = message_content["text"]
        
        user = get_user(telegram_id)
        
        print('User: ', user)
        
        if user is None:
            if is_command(text):
                return handle_command(message_content)
        else:
            isExpense = is_expense(text)
            
            if isExpense:
                return {"status": "saved", "data": response}

    except Exception as e:
        print(f"Error when processing message with LangChain: {e}")
        return {"status": "error", "message": str(e)}