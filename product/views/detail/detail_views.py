from rest_framework import permissions, generics
from rest_framework.response import Response

from product.models import ProductCharacteristicCombination
from product.serializers import ProductCharacteristicCombinationSerializer


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductCharacteristicCombinationSerializer
    # queryset = Product.objects.all()
    queryset = ProductCharacteristicCombination.objects.all()
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
