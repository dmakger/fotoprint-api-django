from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views.all.all_product_view import AllProductView
from product.views.combination.product_combination_views import ProductCombinationsView
from product.views.detail.detail_views import ProductDetailView
from product.views.form.product_form_views import ProductFormCombinationsView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    #  Проекты
    path("all/", AllProductView.as_view({'get': 'all'})),
    path('all/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Комбинации
    path('combinations/<int:pk>/', ProductCombinationsView.as_view({'get': 'get_characteristics'})),

    # Формы
    path('forms/<int:pk>/', ProductFormCombinationsView.as_view({'get': 'get_forms'})),
]
