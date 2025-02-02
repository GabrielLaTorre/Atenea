from models.user_model import create_user

def handle_command(data):
    command = data["text"]
    
    if command == "/start":
        welcome_message = """Hi! 👋 I'm your financial assistant.
                            Use the /register command to get started.
                            Once registered, you can easily start adding your expenses."""
        return welcome_message
    if command == "/register":
        telegram_id = data["chatId"]
        create_user(telegram_id)
    else:
        print("Comando no reconocido:", command)
        
def is_command(message_text):
    return message_text.startswith("/")
