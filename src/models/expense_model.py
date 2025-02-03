from config.database import get_supabase_client

def create_expense(description, amount, category):
    supabase = get_supabase_client()

    data = {
        "description": description,
        "amount": amount,
        "category": category,
        "added_at": "now()"
    }
    
    response = supabase.table("expenses").insert(data).execute()
    return response
