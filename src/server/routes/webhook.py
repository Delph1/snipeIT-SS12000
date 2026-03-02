from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from src.server.models.webhook_event import WebhookEvent
from src.server.services.ss12000_service import fetch_updated_entity
from src.server.services.snipeit_service import sync_user_to_snipeit, sync_group_to_snipeit
from src.server.utils.config import WEBHOOK_SECRET
from src.server.utils.logger import log_info, log_error

webhook_bp = Blueprint("webhook", __name__)

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@webhook_bp.route("/webhook", methods=["POST"])
@jwt_required()
@limiter.limit("200 per day")
def handle_webhook():
    """Handle incoming webhook notifications from SS12000."""
    signature = request.headers.get("X-SS12000-Signature")
    if signature != WEBHOOK_SECRET:
        log_error("Invalid webhook signature")
        return jsonify({"error": "Invalid signature"}), 403

    data = request.json
    event = WebhookEvent.from_dict(data, signature)
    log_info(f"Received webhook for {event.entity_type} with ID {event.entity_id}")

    # Fetch updated data from SS12000
    updated_data = fetch_updated_entity(event.entity_type, event.entity_id)
    if not updated_data:
        return jsonify({"error": "Could not fetch updated data"}), 500

    # Synchronize with Snipe-IT
    if event.entity_type == "Person":
        success = sync_user_to_snipeit(updated_data)
    elif event.entity_type == "Group":
        success = sync_group_to_snipeit(updated_data)
    else:
        log_error(f"Unknown entity type: {event.entity_type}")
        return jsonify({"error": "Unknown entity type"}), 400

    if success:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"error": "Synchronization failed"}), 500
