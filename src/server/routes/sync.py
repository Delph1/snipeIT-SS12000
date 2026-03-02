from flask import Blueprint, jsonify
from src.server.services.ss12000_service import fetch_updated_entity
from src.server.services.snipeit_service import sync_user_to_snipeit, sync_group_to_snipeit
from src.server.utils.logger import log_info, log_error

sync_bp = Blueprint("sync", __name__)

@sync_bp.route("/sync/<entity_type>/<entity_id>", methods=["POST"])
def manual_sync(entity_type: str, entity_id: str):
    """Manual synchronization of an entity."""
    log_info(f"Manual synchronization of {entity_type} with ID {entity_id}")

    # Fetch updated data from SS12000
    updated_data = fetch_updated_entity(entity_type, entity_id)
    if not updated_data:
        return jsonify({"error": "Could not fetch updated data"}), 500

    # Synchronize with Snipe-IT
    if entity_type == "Person":
        success = sync_user_to_snipeit(updated_data)
    elif entity_type == "Group":
        success = sync_group_to_snipeit(updated_data)
    else:
        log_error(f"Unknown entity type: {entity_type}")
        return jsonify({"error": "Unknown entity type"}), 400

    if success:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"error": "Synchronization failed"}), 500
