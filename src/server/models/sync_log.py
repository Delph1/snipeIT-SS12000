from dataclasses import dataclass
from datetime import datetime

@dataclass
class SyncLog:
    entity_type: str
    entity_id: str
    status: str
    timestamp: str = datetime.now().isoformat()

    def to_dict(self):
        return {
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "status": self.status,
            "timestamp": self.timestamp,
        }
