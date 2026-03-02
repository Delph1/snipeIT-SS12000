from src.shared.config import SS12000_JWT_TOKEN, SNIPEIT_API_TOKEN

def get_ss12000_headers():
    return {"Authorization": f"Bearer {SS12000_JWT_TOKEN}"}

def get_snipeit_headers():
    return {"Authorization": f"Bearer {SNIPEIT_API_TOKEN}"}
