from flask import Blueprint, request, jsonify
import hmac
from flask_jwt_extended import jwt_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from src.server.models.webhook_event import WebhookEvent
from src.server.services.sync_service import process_entity_sync
from src.shared.config import WEBHOOK_SECRET
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
    if not signature or not hmac.compare_digest(signature, WEBHOOK_SECRET):
        log_error("Invalid webhook signature")
        return jsonify({"error": "Invalid signature"}), 403

    data = request.json
    event = WebhookEvent.from_dict(data, signature)
    log_info(f"Received webhook for {event.entity_type} with ID {event.entity_id}")

    success = process_entity_sync(event.entity_type, event.entity_id)

    if success:
        return jsonify({"status": "success"}), 200
    else:
        # The specific error is logged in the service layer.
        return jsonify({"error": "Synchronization failed"}), 500
