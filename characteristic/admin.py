from django.contrib import admin


#  ГРУППА ХАРАКТЕРИСТИК
from characteristic.models import GroupCharacteristic, Characteristic, CharacteristicItem


class GroupCharacteristicAdmin(admin.ModelAdmin):
    list_display = ['title', 'number', 'id']


#  ГРУППА ХАРАКТЕРИСТИК
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


#  ГРУППА ХАРАКТЕРИСТИК
class CharacteristicItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'characteristic', 'price', 'id']


admin.site.register(GroupCharacteristic, GroupCharacteristicAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(CharacteristicItem, CharacteristicItemAdmin)
