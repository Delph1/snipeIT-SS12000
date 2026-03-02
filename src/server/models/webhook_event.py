from dataclasses import dataclass
from typing import Optional

@dataclass
class WebhookEvent:
    entity_type: str
    entity_id: str
    timestamp: Optional[str] = None
    signature: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict, signature: str):
        return cls(
            entity_type=data["entityType"],
            entity_id=data["entityId"],
            timestamp=data.get("timestamp"),
            signature=signature,
        )
