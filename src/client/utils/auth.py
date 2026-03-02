from src.shared.config import SS12000_JWT_TOKEN

def get_auth_headers():
    return {"Authorization": f"Bearer {SS12000_JWT_TOKEN}"}
