from django.urls import path

from characteristic.views.form_views import CharacteristicAutocomplete

urlpatterns = [
    path('characteristic-autocomplete/', CharacteristicAutocomplete.as_view(), name='characteristic-autocomplete'),
]
