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

# BoL API Configuration
BOL_API_BASE = os.getenv("BOL_API_BASE", "https://api.bol-example.com")
BOL_API_TOKEN = os.getenv("BOL_API_TOKEN", "")
BOL_CLIENT_ID = os.getenv("BOL_CLIENT_ID", "client.se")
BOL_PROVIDER_ID = os.getenv("BOL_PROVIDER_ID", "serviceprovider.se")
BOL_SCHOOL_ID = os.getenv("BOL_SCHOOL_ID", "12345678")

# JWT Configuration
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecretkey")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = os.getenv("LOG_FORMAT", "%(asctime)s - %(levelname)s - %(message)s")