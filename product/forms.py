from product.models import ProductCharacteristicCombination, Product
from dal import autocomplete
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'category': autocomplete.ModelSelect2(url='category-autocomplete'),
        }


class ProductCharacteristicCombinationForm(forms.ModelForm):
    class Meta:
        model = ProductCharacteristicCombination
        fields = '__all__'
        widgets = {
            'combination': autocomplete.ModelSelect2(url='combination-autocomplete'),
        }
