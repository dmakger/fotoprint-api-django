from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from product.models import GroupProduct


class AllProductView(viewsets.ModelViewSet):
    # serializer_class = ProjectSerializer
    queryset = GroupProduct.objects.all()
    permission_classes = [permissions.AllowAny]
    # filter = ProjectFilter
    # error = ProjectError()

    # Получение всех проектов
    @action(methods=['get'], detail=False)
    def all(self, request):
        filter_data = self.filter(request)