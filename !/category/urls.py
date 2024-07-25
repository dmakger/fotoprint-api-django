from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category.views import AllCategoryView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    #  ВСЕ Категории
    path("all/", AllCategoryView.as_view({'get': 'all'})),
]
