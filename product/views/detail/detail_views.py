from rest_framework import permissions, generics
from rest_framework.response import Response

from product.models import Product
from product.views.detail.detail_serializers import ProductDetailSerializer


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]

    # Получение всех продуктов
    def get_serializer_context(self):
        context = super().get_serializer_context()
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user.profile
        context['user'] = user
        return context

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # add_count_product_chart(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
