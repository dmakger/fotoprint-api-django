from dal import autocomplete
from characteristic.models import Characteristic, Combination


class CharacteristicAutocomplete(autocomplete.Select2QuerySetView):
    """
    Выдает список `Characteristic` по указанному `characteristic_group`
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Characteristic.objects.none()

        qs = Characteristic.objects.all()

        characteristic_group = self.forwarded.get('characteristic_group', None)
        if characteristic_group:
            qs = qs.filter(characteristic_group=characteristic_group)

        if self.q:
            qs = qs.filter(title__icontains=self.q)

        return qs


class CombinationAutocomplete(autocomplete.Select2QuerySetView):
    """
    Выдает список `Combination` по указанному `combination`
    """

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Combination.objects.none()

        qs = Combination.objects.all()

        if self.q:
            qs = qs.filter(characteristic__title__icontains=self.q)
        return qs

    def get_result_label(self, item):
        return item.get_full_path()
