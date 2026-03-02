import requests
from src.server.utils.auth import get_ss12000_headers
from src.server.utils.logger import log_info, log_error
from src.server.utils.config import SS12000_API_BASE

def fetch_updated_entity(entity_type: str, entity_id: str) -> dict:
    """Fetch an updated entity from the SS12000 API."""
    try:
        response = requests.get(
            f"{SS12000_API_BASE}/{entity_type.lower()}/{entity_id}",
            headers=get_ss12000_headers(),
        )
        response.raise_for_status()
        log_info(f"Fetched updated {entity_type} with ID {entity_id}")
        return response.json()
    except requests.exceptions.RequestException as e:
        log_error(f"Error fetching {entity_type} {entity_id}: {e}")
        return {}
