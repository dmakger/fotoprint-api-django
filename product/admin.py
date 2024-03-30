from django.contrib import admin
from product.models import Product, ProductToCharacteristicItem


#  ПРОДУКТ
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'execution_time', 'id']


# ПРОДУКТ к ЭЛЕМЕНТУ ХАРАКТЕРИСТИК
class ProductToCharacteristicItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'characteristic_item', 'group_characteristic', 'price', 'number', 'id']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductToCharacteristicItem, ProductToCharacteristicItemAdmin)
