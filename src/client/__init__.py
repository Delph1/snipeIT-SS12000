import requests
import os
from src.client.ss12000_client import SS12000Client

MY_SERVER_URL = os.getenv("WEBHOOK_URL", "http://webhooks_server:5000/webhook")

def main():
    client = SS12000Client()

    entities = ["Person", "Group"]
    client.register_webhook(entities)
    print("Webhook registered.")

    users = client.fetch_users(limit=100)
    print(f"Fetched {len(users)} users from SS12000. Starting sync...")

    for user in users:
        try:
            sync_url = f"{MY_SERVER_URL}/sync/Person/{user.id}"
            response = requests.post(sync_url)
            if response.status_code == 200:
                print(f"Successfully synced user {user.id}")
            else:
                print(f"Failed to sync user {user.id}: {response.text}")
        except Exception as e:
            print(f"Error calling sync endpoint for {user.id}: {e}")

if __name__ == "__main__":
    main()
