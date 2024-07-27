from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views.all.all_product_view import AllProductView
from product.views.detail.detail_views import ProductDetailView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    #  Проекты
    path("all/", AllProductView.as_view({'get': 'all'})),
    path('all/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
