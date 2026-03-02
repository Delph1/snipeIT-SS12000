from flask import Blueprint, jsonify
from src.server.services.sync_service import process_entity_sync
from src.server.utils.logger import log_info, log_error

sync_bp = Blueprint("sync", __name__)

@sync_bp.route("/sync/<entity_type>/<entity_id>", methods=["POST"])
def manual_sync(entity_type: str, entity_id: str):
    """Manual synchronization of an entity."""
    log_info(f"Manual synchronization of {entity_type} with ID {entity_id}")

    success = process_entity_sync(entity_type, entity_id)

    if success:
        return jsonify({"status": "success"}), 200
    else:
        # The specific error is logged in the service layer.
        return jsonify({"error": "Synchronization failed"}), 500
