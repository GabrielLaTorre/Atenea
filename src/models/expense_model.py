from config.database import get_supabase_client

def create_expense(data):
    supabase = get_supabase_client()

    response = supabase.table("expenses").insert(data).execute()
    
    return response
