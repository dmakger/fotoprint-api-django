from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from product.filter import ProductCharacteristicCombinationFilter
from product.models import Product, ProductCharacteristicCombination
from product.serializers import ProductSerializer, ProductCharacteristicCombinationSerializer


class AllProductView(viewsets.ModelViewSet):
    serializer_class = ProductCharacteristicCombinationSerializer
    queryset = Product.objects.all()  # Используем модель Product
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductCharacteristicCombinationFilter
    ordering_fields = ['product__title', 'price']  # Поля для сортировки
    ordering = ['product__title']

    # Получение всех продуктов
    @action(methods=['get'], detail=False)
    def all(self, request, **kwargs):
        # queryset = self.filter_queryset(Product.objects.all())  # Применяем фильтры
        queryset = self.filter_queryset(ProductCharacteristicCombination.objects.filter(show_as_product=True))  # Применяем фильтры
        page = self.paginate_queryset(queryset)  # Применяем пагинацию
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
