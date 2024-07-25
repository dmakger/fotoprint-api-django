from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from characteristic.models import CharacteristicGroup, Characteristic, Combination


class CharacteristicGroupAdmin(admin.ModelAdmin):
    """ГРУППА ХАРАКТЕРИСТИК"""
    list_display = ['title', 'id']


class CharacteristicAdmin(admin.ModelAdmin):
    """ХАРАКТЕРИСТИКА"""
    list_display = ['title', 'id']


admin.site.register(CharacteristicGroup, CharacteristicGroupAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Combination, DraggableMPTTAdmin)

