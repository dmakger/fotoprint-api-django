from dal import autocomplete
from characteristic.models import Characteristic, Combination
from product.models import ProductCharacteristicCombination


class CombinationAutocomplete(autocomplete.Select2QuerySetView):
    """
    Выдает список `Combination` по указанному `combination`
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Combination.objects.none()

        qs = Combination.objects.all()

        combination = self.forwarded.get('combination', None)
        if combination:
            qs = qs.filter(characteristic=combination.characteristic)

        if self.q:
            qs = qs.filter(combination__characteristic__title__icontains=self.q)
        print("Queryset:", qs)  # Отладочный вывод

        return qs

    def get_result_label(self, item):
        return item.get_full_path()
