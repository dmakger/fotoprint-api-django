from django.urls import path

from characteristic.views_form import CharacteristicAutocomplete

urlpatterns = [
    path('characteristic-autocomplete/', CharacteristicAutocomplete.as_view(), name='characteristic-autocomplete'),
]
