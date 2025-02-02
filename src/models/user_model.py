from config.database import get_supabase_client


def get_user(telegram_id):
    supabase = get_supabase_client()

    response = supabase.table("users").select("*").eq("telegram_id", telegram_id).limit(1).execute()
    
    if len(response.data) == 0:
        return None
    
    return response.data[0]

def create_user(telegram_id):
    supabase = get_supabase_client()

    response = supabase.table("users").insert({"telegram_id": telegram_id}).execute()
    
    return response.data