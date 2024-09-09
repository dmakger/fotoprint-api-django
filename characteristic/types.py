from dataclasses import dataclass, field
from typing import List

from django.db.models import QuerySet

from characteristic.models import Combination


@dataclass
class CombineType:
    characteristic_group: str
    characteristics: List[str] = field(default_factory=list)

# cs = CombineType(characteristic_group="Group1", characteristics=["char1", "char2", "char3"])


@dataclass
class CombinationWithActiveType:
    combinations: List[QuerySet[Combination]] = field(default_factory=list)
    active_ids: List[int] = field(default_factory=list)
    active_characteristic_ids: List[int] = field(default_factory=list)
