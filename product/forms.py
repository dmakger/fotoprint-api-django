from product.models import ProductCharacteristicCombination
from dal import autocomplete
from django import forms


class ProductCharacteristicCombinationForm(forms.ModelForm):
    class Meta:
        model = ProductCharacteristicCombination
        fields = '__all__'
        widgets = {
            'combination': autocomplete.ModelSelect2(url='combination-autocomplete', forward=['combination']),
        }
