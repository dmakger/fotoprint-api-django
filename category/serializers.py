from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'children']
