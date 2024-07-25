from characteristic.models import CharacteristicGroup
from characteristic.types import CombineType


def created_characteristic_combine(combine: CombineType):
    characteristic_group, created = CharacteristicGroup.objects.get_or_create(title=combine.characteristic_group)
