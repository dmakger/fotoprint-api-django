from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category.form_views import CategoryAutocomplete
from category.views import AllCategoryView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # FORMS
    path('category-autocomplete/', CategoryAutocomplete.as_view(), name='category-autocomplete'),

    #  ВСЕ Категории
    path("all/", AllCategoryView.as_view({'get': 'all'})),
]
