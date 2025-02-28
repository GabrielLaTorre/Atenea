from models.user_model import create_user
from utils.message_response import get_message_response, Responses

def handle_command(data):
    command = data["text"]
    
    if command == "/start":
        return {
                "chat_id": data["chatId"],
                "message": get_message_response(Responses.WELCOME)
                }
    if command == "/register":
        telegram_id = data["chatId"]
        
        create_user(telegram_id)
        
        return {
                "chat_id": telegram_id,
                "message": get_message_response(Responses.REGISTERED)
                }
    else:
        print("Unrecognized command:", command)
        
def is_command(message_text):
    return message_text.startswith("/")
