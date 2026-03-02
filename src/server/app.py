from flask import Flask, jsonify
from src.server.routes.webhook import webhook_bp
from src.server.routes.sync import sync_bp
from src.server.utils.logger import log_info
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from src.server.utils.config import JWT_SECRET_KEY

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
jwt = JWTManager(app)

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

app.register_blueprint(webhook_bp)
app.register_blueprint(sync_bp)

@app.route("/health", methods=["GET"])
def health_check():
    """Health check for the server."""
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    log_info("Starting receiving server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
