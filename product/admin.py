from django.contrib import admin
from product.models import GroupProduct, BaseProduct, Product, CharacteristicProduct, CharacteristicProductItem


# ОСНОВА ДЛЯ ПРОДУКТОВ. От неё продукты наследуют информацию о продукте
class BaseProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'id']


# ГРУППА ПРОДУКТОВ. Показывает все возможные продукты под
class GroupProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'base', 'number', 'id']


# ПРОДУКТ
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'group', 'image', 'price', 'execution_time', 'number', 'id']


# ХАРАКТЕРИСТИКА ПРОДУКТА
class CharacteristicProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'group_characteristic', 'number', 'id']


# ХАРАКТЕРИСТИКА ПРОДУКТА
class CharacteristicProductItemAdmin(admin.ModelAdmin):
    list_display = ['characteristic_product', 'characteristic_item', 'price', 'number', 'id']



admin.site.register(BaseProduct, BaseProductAdmin)
admin.site.register(GroupProduct, GroupProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CharacteristicProduct, CharacteristicProductAdmin)
admin.site.register(CharacteristicProductItem, CharacteristicProductItemAdmin)
