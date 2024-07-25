from django.urls import path
from .views import CharacteristicAutocomplete

urlpatterns = [
    path('characteristic-autocomplete/', CharacteristicAutocomplete.as_view(), name='characteristic-autocomplete'),
]
