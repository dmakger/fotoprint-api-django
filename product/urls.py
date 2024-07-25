from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views.all.all_product_view import AllProductView
from product.views.form_views import CombinationAutocomplete, CategoryAutocomplete

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    path('combination-autocomplete/', CombinationAutocomplete.as_view(), name='combination-autocomplete'),
    path('category-autocomplete/', CategoryAutocomplete.as_view(), name='category-autocomplete'),

    #  Проекты
    path("all/", AllProductView.as_view({'get': 'all'})),
]
