from rest_framework import serializers

from category.serializers import CategorySerializer
from characteristic.serializers import CombinationSerializer, ExecutionTimeSerializer
from product.models import Product, ProductCharacteristicCombination


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализация `Product`
    """
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ProductCharacteristicCombinationSerializer(serializers.ModelSerializer):
    """
    Сериализация `ProductCharacteristicCombination`
    """
    product = ProductSerializer()
    combination = CombinationSerializer()
    execution_time = ExecutionTimeSerializer()

    class Meta:
        model = ProductCharacteristicCombination
        fields = '__all__'
