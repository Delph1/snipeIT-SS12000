import requests
from src.server.utils.auth import get_snipeit_headers
from src.server.utils.logger import log_info, log_error
from src.server.utils.config import SNIPEIT_API_BASE

def sync_user_to_snipeit(user_data: dict) -> bool:
    """Synchronize a user to Snipe-IT."""
    try:
        # Create or update the user in Snipe-IT
        payload = {
            "name": f"{user_data['givenName']} {user_data['familyName']}",
            "email": user_data.get("emails", [{}])[0].get("value"),
            "username": user_data["id"],
        }
        response = requests.post(
            f"{SNIPEIT_API_BASE}/users",
            json=payload,
            headers=get_snipeit_headers(),
        )
        response.raise_for_status()
        log_info(f"Synchronized user {user_data['id']} to Snipe-IT")
        return True
    except requests.exceptions.RequestException as e:
        log_error(f"Error synchronizing user {user_data['id']}: {e}")
        return False

def sync_group_to_snipeit(group_data: dict) -> bool:
    """Synchronize a group to Snipe-IT as a license."""
    try:
        # Create or update the license in Snipe-IT
        payload = {
            "name": group_data["displayName"],
            "serial": group_data["id"],
            "model_id": 1,  # Example: ID for license model
            "status_id": 1,  # Active
        }
        response = requests.post(
            f"{SNIPEIT_API_BASE}/licenses",
            json=payload,
            headers=get_snipeit_headers(),
        )
        response.raise_for_status()
        log_info(f"Synchronized group {group_data['id']} to Snipe-IT")
        return True
    except requests.exceptions.RequestException as e:
        log_error(f"Error synchronizing group {group_data['id']}: {e}")
        return False
