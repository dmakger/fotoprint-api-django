from django.db.models import QuerySet
from rest_framework import serializers

from category.serializers import CategorySerializer
from characteristic.serializers import CombinationSerializer, CharacteristicSerializer
from product.models import Product, ProductCharacteristicCombination, ProductForm
from product.serializers import ProductCharacteristicCombinationSerializer, \
    ProductCharacteristicAllCombinationsSerializer, ProductFormAllCombinationsSerializer, ProductAllFormSerializer


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    Сериализация детальной страницы `Product`
    """
    category = CategorySerializer()
    combinations = serializers.SerializerMethodField()
    forms = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_combinations(self, instance: Product):
        qs: QuerySet[ProductCharacteristicCombination] = ProductCharacteristicCombination.objects.filter(product=instance)
        return ProductCharacteristicAllCombinationsSerializer(qs, many=True).data

    def get_forms(self, instance: Product):
        qs: QuerySet[ProductForm] = ProductForm.objects.filter(product=instance)
        return ProductAllFormSerializer(qs, many=True).data

