from dataclasses import dataclass
from typing import List

@dataclass
class Webhook:
    url: str
    entities: List[str]
    secret: str

    def to_dict(self):
        return {
            "url": self.url,
            "entities": self.entities,
            "secret": self.secret,
        }