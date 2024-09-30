from django.db.models import QuerySet
from rest_framework import serializers

from characteristic.admin import CombinationAdmin
from characteristic.models import Combination
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

    def get_forms(self, instance: ProductForm):
        pf_combinations: QuerySet[ProductFormCombination] = ProductFormCombination.objects.filter(product_form=instance)
        # combinations = Combination.objects.filter(productformcombination__product_form=instance)
        # print(combinations)
        for x in pf_combinations:
            print(x.combination.get_full_children())
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
