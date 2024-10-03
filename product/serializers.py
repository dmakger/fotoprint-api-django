from django.db.models import QuerySet
from mptt.querysets import TreeQuerySet
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from api.settings import MEDIA_URL
from category.serializers import CategorySerializer
from characteristic.models import Combination, Characteristic
from characteristic.serializers import ExecutionTimeSerializer, CharacteristicSerializer, CharacteristicGroupSerializer, \
    CombinationSerializer
from characteristic.types import CombinationWithActiveType
from lib.combinations_lib import get_parents_combination_by_product, get_combinations_as_dict_id, \
    get_product_combination_id
from product.models import Product, ProductCharacteristicCombination, ProductFormCombination, ProductForm, \
    ProductCharacteristicCombinationImage


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
    title = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    parentId = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    executionTime = serializers.SerializerMethodField()
    # combinations = serializers.SerializerMethodField()

    class Meta:
        model = ProductCharacteristicCombination
        fields = ['id', 'title', 'price', 'image', 'images', 'parentId', 'category', 'executionTime']

    def get_title(self, instance: ProductCharacteristicCombination):
        return instance.get_title()

    def get_image(self, instance: ProductCharacteristicCombination):
        return instance.get_main_image()

    def get_images(self, instance: ProductCharacteristicCombination):
        images = ProductCharacteristicCombinationImage.objects.filter(
            product_characteristic_combination=instance, is_main=False
        ).values_list('image', flat=True)
        return [f"{MEDIA_URL}{x}" for x in images]

    def get_parentId(self, instance: ProductCharacteristicCombination):
        return instance.product.id

    def get_category(self, instance: ProductCharacteristicCombination):
        return CategorySerializer(instance.product.category).data

    def get_executionTime(self, instance: ProductCharacteristicCombination):
        return ExecutionTimeSerializer(instance.execution_time).data


class ProductCharacteristicAllCombinationsSerializer(serializers.ModelSerializer):
    """
    Сериализация `ProductCharacteristicCombination`.
    Добавляет `characteristics` список всех характеристик в данной комбинации
    """
    # product = ProductSerializer()
    characteristics = serializers.SerializerMethodField()
    forms = serializers.SerializerMethodField()
    execution_time = ExecutionTimeSerializer()

    class Meta:
        model = ProductCharacteristicCombination
        # fields = ['id', 'product', 'price', 'characteristics', 'execution_time']
        fields = ['id', 'price', 'characteristics', 'forms', 'execution_time']

    def get_characteristics(self, instance: ProductCharacteristicCombination):
        characteristics = instance.combination.get_full_children()
        return CharacteristicSerializer(characteristics, many=True).data

    def get_forms(self, instance: ProductCharacteristicCombination):
        forms = ProductForm.objects.filter(product=instance)
        return ProductAllFormSerializer(forms, many=True).data


class ProductCombinationSerializer(serializers.ModelSerializer):
    """
    Сериализация `ProductCharacteristicCombination`.
    Добавляет `characteristics` список всех характеристик в данной комбинации
    """
    # product = ProductSerializer()
    image = serializers.SerializerMethodField()
    combinations = serializers.SerializerMethodField()
    execution_time = ExecutionTimeSerializer()

    class Meta:
        model = ProductCharacteristicCombination
        # fields = ['id', 'product', 'price', 'characteristics', 'execution_time']
        fields = ['id', 'price', 'image', 'combinations', 'execution_time']

    def get_image(self, instance: ProductCharacteristicCombination):
        return instance.get_main_image()

    def get_combinations(self, instance: ProductCharacteristicCombination):
        res: CombinationWithActiveType = instance.combination.get_children_as_mtrx()
        combinations = res.combinations + [get_parents_combination_by_product(instance.product)]
        product_combination_id_to_combination_ids = get_combinations_as_dict_id(instance.product)
        active_ids = res.active_ids
        active_characteristic_ids = res.active_characteristic_ids
        serializers_data = []
        for i in range(len(combinations)):
            combination_serializer_data = CombinationSerializer(
                combinations[i],
                context={'active_id': active_ids[i]},
                many=True
            ).data
            updated_serializer_data = []
            for sd in combination_serializer_data:
                current_ids = [*active_characteristic_ids[:i], sd['characteristic']['id'], *active_characteristic_ids[i+1:]]
                updated_serializer_data.append({
                    **sd,
                    'productCombinationId': get_product_combination_id(product_combination_id_to_combination_ids,
                                                                  current_ids)
                 })
            # print([{"id": x['id'], "title": x['characteristic']['title']} for x in updated_serializer_data])
            serializers_data.append(updated_serializer_data)
        return reversed(serializers_data)


class ProductFormAllCombinationsSerializer(serializers.ModelSerializer):
    """
    Сериализация `ProductFormCombination`.
    Добавляет `characteristics` список всех характеристик в данной комбинации
    """
    # product = ProductSerializer()
    characteristics = serializers.SerializerMethodField()
    execution_time = ExecutionTimeSerializer()

    class Meta:
        model = ProductFormCombination
        # fields = ['id', 'product_form', 'characteristics', 'execution_time']
        fields = ['id', 'characteristics', 'execution_time']

    def get_characteristics(self, instance: ProductFormCombination):
        characteristics = instance.combination.get_full_children()
        return CharacteristicSerializer(characteristics, many=True).data


class ProductAllFormSerializer(serializers.ModelSerializer):
    """
    Сериализация `ProductFormCombination`.
    Добавляет `characteristics` список всех характеристик в данной комбинации
    """
    # product = ProductSerializer()
    combinations = serializers.SerializerMethodField()

    class Meta:
        model = ProductForm
        # fields = ['id', 'product_form', 'characteristics', 'execution_time']
        fields = ['id', 'title', 'combinations']

    def get_combinations(self, instance: ProductForm):
        forms: QuerySet[ProductFormCombination] = ProductFormCombination.objects.filter(product_form=instance)
        return ProductFormAllCombinationsSerializer(forms, many=True).data