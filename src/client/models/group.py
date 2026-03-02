from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Group:
    id: str
    display_name: str
    group_type: str
    members: Optional[List[str]] = None  # Lista med användar-ID:n

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            display_name=data.get("displayName", ""),
            group_type=data.get("groupType", ""),
            members=[member["person"]["id"] for member in data.get("groupMemberships", [])],
        )