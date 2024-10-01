from django.db.models import QuerySet
from rest_framework import serializers

from characteristic.admin import CombinationAdmin
from characteristic.models import Combination, Characteristic
from characteristic.serializers import ExecutionTimeSerializer, CharacteristicSerializer
from lib.forms_lib import add_characteristics_in_form
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
        updated_data = dict()
        for x in pf_combinations:
            pf_serializer = ProductFormCombinationSerializer(x).data
            characteristics = pf_serializer['characteristics']
            form_data = {
                'id': pf_serializer['id'],
                'price': pf_serializer['price'],
                'execution_time': pf_serializer['execution_time']
            }

            # Берем первую характеристику, если её ещё нет, добавляем
            first_char = characteristics[0]
            if first_char['id'] not in updated_data:
                updated_data[first_char['id']] = {
                    'id': first_char['id'],
                    'title': first_char['title'],
                    'description': first_char['description'],
                    'characteristicGroup': first_char['characteristicGroup'],
                    'children': []
                }

            # Добавляем характеристики в дерево
            add_characteristics_in_form(updated_data[first_char['id']], characteristics[1:], form_data)
        updated_data = list(updated_data.values())
        return updated_data



class ProductFormCombinationSerializer(serializers.ModelSerializer):
    """
    Сериализация `ProductFormCombination`.
    Добавляет `characteristics` список всех характеристик в данной комбинации
    """
    # product = ProductSerializer()
    characteristics = serializers.SerializerMethodField()
    execution_time = ExecutionTimeSerializer()

    class Meta:
        model = ProductFormCombination
        fields = ['id', 'characteristics', 'price', 'execution_time']

    def get_characteristics(self, instance: ProductFormCombination):
        characteristics = instance.combination.get_full_children()
        # print(characteristics)
        return CharacteristicSerializer(characteristics, many=True).data
