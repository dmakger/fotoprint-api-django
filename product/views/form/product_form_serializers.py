from rest_framework import serializers

from characteristic.serializers import ExecutionTimeSerializer
from product.models import ProductForm, ProductFormCombination


class ProductFormSerializer(serializers.ModelSerializer):
    """
    Сериализация `ProductForm`.
    Добавляет `characteristics` список всех характеристик в данной комбинации
    """
    # product = ProductSerializer()
    forms = serializers.SerializerMethodField()

    class Meta:
        model = ProductForm
        fields = ['id', 'title', 'forms']

    def get_forms(self, instance):
        return []


class ProductFormCombinationSerializer(serializers.ModelSerializer):
    """
    Сериализация `ProductFormCombination`.
    Добавляет `characteristics` список всех характеристик в данной комбинации
    """
    # product = ProductSerializer()
    combinations = serializers.SerializerMethodField()
    execution_time = ExecutionTimeSerializer()

    class Meta:
        model = ProductFormCombination
        fields = ['id', 'price', 'combinations', 'execution_time']
