from itertools import product

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from product.models import ProductForm, Product, ProductCharacteristicCombination
from product.views.form.product_form_serializers import ProductFormSerializer


class ProductFormCombinationsView(viewsets.ModelViewSet):
    serializer_class = ProductFormSerializer
    queryset = ProductCharacteristicCombination.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=False)
    def get_forms(self, request, *args, **kwargs):
        instance = self.get_object()
        forms = ProductForm.objects.filter(product=instance)
        serializer = self.get_serializer(forms, many=True)
        return Response(serializer.data)