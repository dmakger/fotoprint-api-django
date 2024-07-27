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
    forms = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_combinations(self, instance: Product):
        qs: QuerySet[ProductCharacteristicCombination] = ProductCharacteristicCombination.objects.filter(product=instance)
        # TODO: Переместить формы во внутрь combinations
        return ProductCharacteristicAllCombinationsSerializer(qs, many=True).data

    def get_forms(self, instance: Product):
        product_ids = ProductCharacteristicCombination.objects.filter(product=instance).values_list('product_id',
                                                                                                    flat=True)
        forms = ProductForm.objects.filter(product_id__in=product_ids)
        return ProductAllFormSerializer(forms, many=True).data


