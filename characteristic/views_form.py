from dal import autocomplete
from .models import Characteristic


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
