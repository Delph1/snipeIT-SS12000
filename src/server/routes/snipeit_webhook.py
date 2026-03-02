from flask import Blueprint, request, jsonify
from src.server.services.bol_service import provision_license_in_bol, return_license_in_bol
from src.server.utils.logger import log_info

snipeit_webhook_bp = Blueprint("snipeit_webhook", __name__)

@snipeit_webhook_bp.route("/snipeit-webhook", methods=["POST"])
def handle_snipeit_webhook():
    """
    Handle incoming webhooks from Snipe-IT.
    Triggers when an asset or license is checked out/in.
    """
    data = request.json
    
    if not data:
        return jsonify({"status": "ignored", "message": "No data received"}), 200

    # Snipe-IT webhook payload structure usually contains 'event', 'item', and 'target'
    event_type = data.get("event")
    item_type = data.get("item", {}).get("type")
    
    log_info(f"Received Snipe-IT webhook: {event_type} for {item_type}")

    # We only care about license events
    if item_type == "license":
        user_data = data.get("target") # The user the license was assigned to
        license_data = data.get("item") # The license itself
        
        if user_data and license_data:
            if event_type == "checkout":
                success = provision_license_in_bol(user_data, license_data)
                if success:
                    return jsonify({"status": "success", "message": "BoL provisioned"}), 200
                else:
                    return jsonify({"status": "error", "message": "BoL provisioning failed"}), 500
            elif event_type == "checkin":
                success = return_license_in_bol(user_data, license_data)
                if success:
                    return jsonify({"status": "success", "message": "BoL returned"}), 200
                else:
                    return jsonify({"status": "error", "message": "BoL return failed"}), 500
                
    return jsonify({"status": "ignored"}), 200
