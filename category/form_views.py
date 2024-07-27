from dal import autocomplete

from category.models import Category


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
