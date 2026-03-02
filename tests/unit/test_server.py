import unittest
from unittest.mock import patch, MagicMock
from src.server.routes.webhook import handle_webhook
from src.server.models.webhook_event import WebhookEvent

class TestWebhookRoute(unittest.TestCase):
    @patch("src.server.routes.webhook.request")
    @patch("src.server.services.ss12000_service.fetch_updated_entity")
    @patch("src.server.services.snipeit_service.sync_user_to_snipeit")
    def test_handle_webhook_user(
        self, mock_sync_user, mock_fetch_entity, mock_request
    ):
        # Mock request object
        mock_request.json = {"entityType": "Person", "entityId": "123"}
        mock_request.headers = {"X-SS12000-Signature": "<YOUR_SECRET_KEY>"}

        # Mock API response
        mock_fetch_entity.return_value = {
            "id": "123",
            "givenName": "Kalle",
            "familyName": "Svensson",
        }
        mock_sync_user.return_value = True

        # Call the function
        response = handle_webhook()

        # Verify the result
        self.assertEqual(response[1], 200)
        mock_fetch_entity.assert_called_once_with("Person", "123")
        mock_sync_user.assert_called_once()

if __name__ == "__main__":
    unittest.main()
