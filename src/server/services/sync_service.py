from src.server.services.ss12000_service import fetch_updated_entity
from src.server.services.snipeit_service import sync_user_to_snipeit, sync_group_to_snipeit
from src.server.utils.logger import log_error

def process_entity_sync(entity_type: str, entity_id: str) -> bool:
    """
    Fetches an entity from SS12000 and synchronizes it to Snipe-IT.

    This is a shared service function to avoid code duplication between the
    webhook handler and the manual sync endpoint.
    """
    # Fetch updated data from SS12000
    updated_data = fetch_updated_entity(entity_type, entity_id)
    if not updated_data:
        # Error is already logged by fetch_updated_entity
        return False

    # Synchronize with Snipe-IT
    if entity_type == "Person":
        return sync_user_to_snipeit(updated_data)
    elif entity_type == "Group":
        return sync_group_to_snipeit(updated_data)
    else:
        log_error(f"Unknown entity type for sync: {entity_type}")
        return False
