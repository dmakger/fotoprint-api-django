from dal import autocomplete

from category.models import Category
from characteristic.models import Characteristic, Combination
from product.models import ProductCharacteristicCombination


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    """
    Выдает список `Category`
    """

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Category.objects.none()

        qs = Category.objects.all()

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
