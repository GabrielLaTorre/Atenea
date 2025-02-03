from models.user_model import create_user
from utils.message_response import get_message_response, Responses

def handle_command(data):
    command = data["text"]
    
    if command == "/start":
        return get_message_response(Responses.WELCOME)
    if command == "/register":
        telegram_id = data["chatId"]
        
        create_user(telegram_id)
        
        return get_message_response(Responses.REGISTERED)
    else:
        print("Comando no reconocido:", command)
        
def is_command(message_text):
    return message_text.startswith("/")
