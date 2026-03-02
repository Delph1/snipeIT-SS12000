# tests/unit/test_client.py

import unittest
from unittest.mock import patch, MagicMock
from src.client.ss12000_client import SS12000Client
from src.client.models.person import Person

class TestSS12000Client(unittest.TestCase):
    @patch("requests.get")
    def test_fetch_users(self, mock_get):
        # Mock API response
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                "id": "123",
                "givenName": "Kalle",
                "familyName": "Svensson",
                "civicNo": {"value": "199001011234"},
                "emails": [{"value": "kalle@example.com"}],
            }
        ]
        mock_get.return_value = mock_response

        client = SS12000Client()
        users = client.fetch_users(limit=1)

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].given_name, "Kalle")
        self.assertEqual(users[0].email, "kalle@example.com")

    @patch("requests.post")
    def test_register_webhook(self, mock_post):
        # Mock API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        client = SS12000Client()
        response = client.register_webhook(["Person"])

        self.assertEqual(response["status"], "success")

if __name__ == "__main__":
    unittest.main()
