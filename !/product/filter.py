import django_filters
from django.db.models import Q

from .models import Product


class ProductFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='search_by_all_fields', label='Поиск по всем полям')

    class Meta:
        model = Product
        fields = {
            'title': ['icontains'],
            # 'category__title': ['icontains'],
        }

    def search_by_all_fields(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(group__base__category__title__icontains=value)
            # Добавьте другие поля вашей модели, если это необходимо
        )
