import django_filters
from django.db.models import Q
from .models import ProductCharacteristicCombination


class ProductCharacteristicCombinationFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='search_by_all_fields', label='Поиск по всем полям')

    class Meta:
        model = ProductCharacteristicCombination
        fields = {
            'product__title': ['icontains'],
            # 'category__title': ['icontains'],
        }

    def search_by_all_fields(self, queryset, name, value):
        return queryset.filter(
            Q(product__title__icontains=value) |
            Q(product__category__title__icontains=value)
        )
