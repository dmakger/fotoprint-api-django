from dataclasses import dataclass, field
from typing import List


@dataclass
class CombineType:
    characteristic_group: str
    characteristics: List[str] = field(default_factory=list)

# cs = CombineType(characteristic_group="Group1", characteristics=["char1", "char2", "char3"])
