import requests
import uuid
from src.shared.config import BOL_API_BASE, BOL_API_TOKEN, BOL_CLIENT_ID, BOL_PROVIDER_ID, BOL_SCHOOL_ID
from src.server.utils.logger import log_info, log_error

def provision_license_in_bol(user_data: dict, license_data: dict) -> bool:
    """
    Calls the BoL API to provision a license for a user based on Snipe-IT data.
    """
    try:
        assignment_id = str(uuid.uuid4())
        
        article_number = license_data.get("name")
        user_id = user_data.get("username")

        payload = {
            "clientId": BOL_CLIENT_ID,
            "serviceProviderId": BOL_PROVIDER_ID,
            "school": {
                "idSource": "skolverket",
                "id": BOL_SCHOOL_ID
            },
            "assignments": [
                {
                    "clientAssignmentId": assignment_id,
                    "freeTrial": False,
                    "articleNumber": article_number,
                    "clientOrderLineId": str(license_data.get("id")),
                    "user": {
                        "idSource": "client",
                        "id": user_id
                    }
                }
            ]
        }
        
        response = requests.post(
            f"{BOL_API_BASE}/v1/assignments/create",
            json=payload,
            headers={"Authorization": f"Bearer {BOL_API_TOKEN}"}
        )
        response.raise_for_status()
        
        log_info(f"Provisioned BoL license '{article_number}' for user '{user_id}'")
        return True

    except requests.exceptions.RequestException as e:
        log_error(f"Error provisioning BoL license: {e} - Response: {e.response.text if e.response else 'No response'}")
        return False

def return_license_in_bol(user_data: dict, license_data: dict) -> bool:
    """
    Calls the BoL API to remove a license assignment from a user.
    """
    try:
        # Generate a unique ID for this assignment deletion attempt
        assignment_id = str(uuid.uuid4())
        
        article_number = license_data.get("name")
        user_id = user_data.get("username")

        payload = {
            "clientId": BOL_CLIENT_ID,
            "serviceProviderId": BOL_PROVIDER_ID,
            "school": {
                "idSource": "skolverket",
                "id": BOL_SCHOOL_ID
            },
            "assignments": [
                {
                    "clientAssignmentId": assignment_id,
                    "articleNumber": article_number,
                    "clientOrderLineId": str(license_data.get("id")),
                    "user": {
                        "idSource": "client",
                        "id": user_id
                    }
                }
            ]
        }
        
        response = requests.post(
            f"{BOL_API_BASE}/v1/assignments/delete",
            json=payload,
            headers={"Authorization": f"Bearer {BOL_API_TOKEN}"}
        )
        response.raise_for_status()
        
        log_info(f"Returned BoL license '{article_number}' for user '{user_id}'")
        return True

    except requests.exceptions.RequestException as e:
        log_error(f"Error returning BoL license: {e} - Response: {e.response.text if e.response else 'No response'}")
        return False
