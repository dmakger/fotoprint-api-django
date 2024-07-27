from itertools import chain

from django.db.models import QuerySet
from rest_framework import serializers

from category.serializers import CategoryTreeSerializer
from characteristic.serializers import CombinationSerializer, CharacteristicSerializer
from product.models import Product, ProductCharacteristicCombination, ProductForm
from product.serializers import ProductCharacteristicCombinationSerializer, \
    ProductCharacteristicAllCombinationsSerializer, ProductFormAllCombinationsSerializer, ProductAllFormSerializer


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    Сериализация детальной страницы `Product`
    """
    category = CategoryTreeSerializer()
    combinations = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_combinations(self, instance: Product):
        qs: QuerySet[ProductCharacteristicCombination] = ProductCharacteristicCombination.objects.filter(product=instance)
        return ProductCharacteristicAllCombinationsSerializer(qs, many=True).data
