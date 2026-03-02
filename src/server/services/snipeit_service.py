import requests
import secrets
import string
from src.server.utils.auth import get_snipeit_headers
from src.server.utils.logger import log_info, log_error
from src.shared.config import SNIPEIT_API_BASE

def sync_user_to_snipeit(user_data: dict) -> bool:
    """Synchronize a user to Snipe-IT."""
    try:
        # Create or update the user in Snipe-IT
        emails = user_data.get("emails", [])
        email_value = emails[0].get("value") if emails else None
        
        payload = {
            "name": f"{user_data['givenName']} {user_data['familyName']}",
            "email": email_value,
            "username": user_data["id"],
        }

        # Check if user exists
        search_response = requests.get(
            f"{SNIPEIT_API_BASE}/users?search={user_data['id']}",
            headers=get_snipeit_headers(),
        )
        search_response.raise_for_status()
        
        # Snipe-IT search is fuzzy, so we filter for exact username match
        users_found = search_response.json().get("rows", [])
        existing_user = next((u for u in users_found if u["username"] == user_data["id"]), None)

        if existing_user:
            # Update existing user
            response = requests.patch(
                f"{SNIPEIT_API_BASE}/users/{existing_user['id']}",
                json=payload,
                headers=get_snipeit_headers(),
            )
            response.raise_for_status()
        else:
            # Create new user
            # Snipe-IT usually requires a password on creation. Generating a random one.
            alphabet = string.ascii_letters + string.digits
            payload["password"] = ''.join(secrets.choice(alphabet) for i in range(16))
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
    """Synchronize an SS12000 group to a Snipe-IT group."""
    try:
        group_name = group_data.get("displayName")
        if not group_name:
            log_error(f"Group data for ID {group_data.get('id')} is missing 'displayName'.")
            return False

        # Check if group exists in Snipe-IT by name.
        # Note: The Snipe-IT Group API doesn't have a field for an external ID.
        # We use the group name as a unique identifier for idempotency.
        # This means if a group's name changes in SS12000, a new group will be created in Snipe-IT.
        search_response = requests.get(
            f"{SNIPEIT_API_BASE}/groups",
            params={"name": group_name},
            headers=get_snipeit_headers(),
        )
        search_response.raise_for_status()
        
        search_results = search_response.json()

        if search_results.get("total", 0) > 0:
            log_info(f"Group '{group_name}' (ID: {group_data.get('id')}) already exists in Snipe-IT.")
            # Since name is our key, there's nothing to update.
            return True
        else:
            # Create new group if it doesn't exist
            payload = {
                "name": group_name,
            }
            response = requests.post(
                f"{SNIPEIT_API_BASE}/groups",
                json=payload,
                headers=get_snipeit_headers(),
            )
            response.raise_for_status()
            log_info(f"Created new Snipe-IT group '{group_name}' for SS12000 group ID {group_data.get('id')}")
            
        return True
    except requests.exceptions.RequestException as e:
        log_error(f"Error synchronizing group {group_data.get('id')}: {e} - Response: {e.response.text if e.response else 'No response'}")
        return False
