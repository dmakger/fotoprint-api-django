from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from category.serializers import CategorySerializer
from characteristic.models import Combination, Characteristic
from characteristic.serializers import ExecutionTimeSerializer, CharacteristicSerializer, CharacteristicGroupSerializer
from product.models import Product, ProductCharacteristicCombination, ProductFormCombination, ProductForm


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
    parentId = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    executionTime = serializers.SerializerMethodField()
    # combinations = serializers.SerializerMethodField()

    class Meta:
        model = ProductCharacteristicCombination
        fields = ['id', 'title', 'price', 'image', 'parentId', 'category', 'executionTime']

    def get_title(self, instance: ProductCharacteristicCombination):
        return instance.get_title()

    def get_image(self, instance: ProductCharacteristicCombination):
        return instance.get_image()

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
    characteristics = serializers.SerializerMethodField()
    execution_time = ExecutionTimeSerializer()

    class Meta:
        model = ProductCharacteristicCombination
        # fields = ['id', 'product', 'price', 'characteristics', 'execution_time']
        fields = ['id', 'price', 'characteristics', 'execution_time']

    def get_characteristics(self, instance: ProductCharacteristicCombination):
        combinations = Combination.objects.filter(
            productcharacteristiccombination__product=instance.product
        ).distinct()
        print('qwe', instance, combinations)
        return CombinationCharacteristicRecursiveSerializer(combinations, many=True).data
        # characteristics = instance.combination.get_full_children()
        # return CharacteristicSerializer(characteristics, many=True).data


class CombinationCharacteristicRecursiveSerializer(serializers.ModelSerializer):
    """
    Сериализация `Combination`.
    Добавляет `characteristics` список всех характеристик в данной комбинации
    """
    # product = ProductSerializer()
    characteristic = CharacteristicSerializer()
    children = RecursiveField(many=True)

    class Meta:
        model = Combination
        fields = ['id', 'characteristic', 'children']


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