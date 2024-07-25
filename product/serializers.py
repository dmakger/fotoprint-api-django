from rest_framework import serializers

from category.serializers import CategorySerializer
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
