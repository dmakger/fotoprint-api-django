from rest_framework import serializers

from category.serializers import CategorySerializer
from characteristic.serializers import CombinationSerializer, ExecutionTimeSerializer, CharacteristicSerializer
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


class ProductCharacteristicAllCombinationsSerializer(serializers.ModelSerializer):
    """
    Сериализация `ProductCharacteristicCombination`.
    Добавляет `characteristics` список всех характеристик в данной комбинации
    """
    # product = ProductSerializer()
    characteristics = serializers.SerializerMethodField()
    execution_time = ExecutionTimeSerializer()

    class Meta:
        model = ProductCharacteristicCombination
        # fields = ['id', 'product', 'price', 'characteristics', 'execution_time']
        fields = ['id', 'price', 'characteristics', 'execution_time']

    def get_characteristics(self, instance: ProductCharacteristicCombination):
        characteristics = instance.combination.get_full_children()
        return CharacteristicSerializer(characteristics, many=True).data
