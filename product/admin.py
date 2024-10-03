from django.contrib import admin

from product.forms import ProductCharacteristicCombinationForm, ProductForm as ProductFormForAdmin
from product.models import Product, ProductAdditionalService, ProductCharacteristicCombination, ProductForm, \
    ProductFormCombination, ProductCharacteristicCombinationImage


class ProductAdmin(admin.ModelAdmin):
    """ПРОДУКТ"""
    form = ProductFormForAdmin
    list_display = ['title', 'category', 'id']


class ProductAdditionalServiceAdmin(admin.ModelAdmin):
    """Дополнительные услуги у продуктов"""
    list_display = ['title', 'product', 'price', 'id']


class ProductCharacteristicCombinationAdmin(admin.ModelAdmin):
    """Комбинации характеристик у продукта"""
    form = ProductCharacteristicCombinationForm
    list_display = ['product', 'title', 'combination', 'price', 'execution_time', 'show_as_product', 'id']


class ProductCharacteristicCombinationImageAdmin(admin.ModelAdmin):
    """ПРОДУКТ"""
    list_display = ['product_characteristic_combination', 'image', 'is_main', 'id']


class ProductFormAdmin(admin.ModelAdmin):
    """Форма продукта"""
    list_display = ['product', 'title_admin', 'title', 'id']


class ProductFormCombinationAdmin(admin.ModelAdmin):
    """Форма продукта"""
    list_display = ['product_form', 'combination', 'price', 'execution_time', 'id']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAdditionalService, ProductAdditionalServiceAdmin)
admin.site.register(ProductCharacteristicCombination, ProductCharacteristicCombinationAdmin)
admin.site.register(ProductCharacteristicCombinationImage, ProductCharacteristicCombinationImageAdmin)
admin.site.register(ProductForm, ProductFormAdmin)
admin.site.register(ProductFormCombination, ProductFormCombinationAdmin)
