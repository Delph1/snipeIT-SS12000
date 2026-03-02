import os

# SS12000 Configuration
SS12000_API_BASE = os.getenv("SS12000_URL", "https://api.ss12000.se")
SS12000_JWT_TOKEN = os.getenv("SS12000_JWT_TOKEN", "")

# Webhook Configuration
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "http://localhost:5000/webhook")

# Snipe-IT Configuration
SNIPEIT_API_BASE = os.getenv("SNIPEIT_URL", "http://snipeit:8000/api/v1")
SNIPEIT_API_TOKEN = os.getenv("SNIPEIT_API_TOKEN", "")