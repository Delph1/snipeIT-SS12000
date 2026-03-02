# src/client/ss12000_client.py

import requests
from typing import List, Optional
from src.client.models.person import Person
from src.client.models.group import Group
from src.client.models.webhook import Webhook
from src.client.utils.auth import get_auth_headers
from src.client.utils.logger import log_info, log_error
from src.shared.config import SS12000_API_BASE, WEBHOOK_URL, WEBHOOK_SECRET

class SS12000Client:
    def __init__(self):
        self.base_url = SS12000_API_BASE
        self.headers = get_auth_headers()

    def fetch_users(self, limit: int = 100) -> List[Person]:
        """Fetch a list of users from the SS12000 API."""
        try:
            response = requests.get(
                f"{self.base_url}/persons?limit={limit}",
                headers=self.headers,
            )
            response.raise_for_status()
            users_data = response.json()
            return [Person.from_dict(user) for user in users_data]
        except requests.exceptions.RequestException as e:
            log_error(f"Error fetching users: {e}")
            return []

    def fetch_user_groups(self, user_id: str) -> List[Group]:
        """Fetch groups for a specific user."""
        try:
            response = requests.get(
                f"{self.base_url}/persons/{user_id}/groups",
                headers=self.headers,
            )
            response.raise_for_status()
            groups_data = response.json()
            return [Group.from_dict(group) for group in groups_data]
        except requests.exceptions.RequestException as e:
            log_error(f"Error fetching groups for user {user_id}: {e}")
            return []

    def register_webhook(self, entities: List[str]) -> Optional[dict]:
        """Register a webhook to receive notifications about changes."""
        webhook = Webhook(url=WEBHOOK_URL, entities=entities, secret=WEBHOOK_SECRET)
        try:
            response = requests.post(
                f"{self.base_url}/subscriptions",
                json=webhook.to_dict(),
                headers=self.headers,
            )
            response.raise_for_status()
            log_info(f"Webhook registered for entities: {entities}")
            return response.json()
        except requests.exceptions.RequestException as e:
            log_error(f"Error registering webhook: {e}")
            return None

    def fetch_updated_entity(self, entity_type: str, entity_id: str) -> Optional[dict]:
        """Fetch updated data for a specific entity."""
        try:
            response = requests.get(
                f"{self.base_url}/{entity_type.lower()}/{entity_id}",
                headers=self.headers,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            log_error(f"Error fetching {entity_type} {entity_id}: {e}")
            return None
