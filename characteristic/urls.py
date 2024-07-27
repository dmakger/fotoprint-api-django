from django.urls import path

from characteristic.views.form_views import CharacteristicAutocomplete, CombinationAutocomplete

urlpatterns = [
    # FORMS
    path('characteristic-autocomplete/', CharacteristicAutocomplete.as_view(), name='characteristic-autocomplete'),
    path('combination-autocomplete/', CombinationAutocomplete.as_view(), name='combination-autocomplete'),
]
