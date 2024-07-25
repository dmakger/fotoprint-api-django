from django import forms
from dal import autocomplete
from .models import Combination


class CombinationForm(forms.ModelForm):
    class Meta:
        model = Combination
        fields = ('characteristic_group', 'characteristic', 'parent')
        widgets = {
            'characteristic': autocomplete.ModelSelect2(url='characteristic-autocomplete', forward=['characteristic_group']),
        }
