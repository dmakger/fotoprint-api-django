from django.db.models import QuerySet
from rest_framework import permissions, generics
from rest_framework.response import Response

from product.models import Product, ProductCharacteristicCombination
from product.serializers import ProductCharacteristicAllCombinationsSerializer


class ProductCombinationsDetailView(generics.RetrieveAPIView):
    serializer_class = ProductCharacteristicAllCombinationsSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        qs = ProductCharacteristicCombination.objects.filter(product=instance)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
