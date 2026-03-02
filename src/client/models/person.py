from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
    id: str
    given_name: str
    family_name: str
    civic_no: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            given_name=data.get("givenName", ""),
            family_name=data.get("familyName", ""),
            civic_no=data.get("civicNo", {}).get("value") if data.get("civicNo") else None,
            email=data.get("emails", [{}])[0].get("value") if data.get("emails") else None,
            phone=data.get("phoneNumbers", [{}])[0].get("value") if data.get("phoneNumbers") else None,
        )
