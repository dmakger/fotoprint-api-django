from rest_framework import permissions, generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from product.models import Product, ProductCharacteristicCombination
from product.serializers import ProductCharacteristicAllCombinationsSerializer, ProductCombinationSerializer


class ProductCombinationsDetailView(generics.RetrieveAPIView):
    serializer_class = ProductCharacteristicAllCombinationsSerializer
    queryset = Product.objects.all()
    # queryset = ProductCharacteristicCombination.objects.all()
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        qs = ProductCharacteristicCombination.objects.filter(product=instance)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class ProductCombinationsView(viewsets.ModelViewSet):
    serializer_class = ProductCombinationSerializer
    queryset = ProductCharacteristicCombination.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=False)
    def get_characteristics(self, request, *args, **kwargs):
        instance = self.get_object()  # Получаем объект, с которым работаем
        # Передаем данные из request.data в сериализатор
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
