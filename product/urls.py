from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import AllProductView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    #  Проекты
    path("all/", AllProductView.as_view({'get': 'all'})),
]
