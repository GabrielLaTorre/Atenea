from enum import Enum

class Responses(Enum):
    WELCOME = "WELCOME"
    REGISTERED = "REGISTERED"
    ADDED = "ADDED"
    ERROR = "ERROR"


def get_message_response(message_type, data=""):
    if message_type.value == Responses.WELCOME.value:
        return get_welcome_message()
    elif message_type.value == Responses.REGISTERED.value:
        return get_registered_message()
    elif message_type.value == Responses.ADDED.value:
        return get_added_message(data)
    elif message_type.value == Responses.ERROR.value:
        return get_added_message(data)


def get_welcome_message():
    return """Hi! 👋 I'm your financial assistant.
                Use the /register command to get started.
                Once registered, you can easily start adding your expenses."""
                
def get_registered_message():
    return "You are now registered! 🎉"

def get_added_message(category):
    return f"[{category}] Expense added! ✅"

def get_error_message():
    return "Something didn't go as expected. Please try again. ⚠️"