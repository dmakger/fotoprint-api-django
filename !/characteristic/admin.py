from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import CharacteristicGroup, Characteristic, Combination
from .forms import CombinationForm


class CharacteristicGroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


class CombinationAdmin(DraggableMPTTAdmin):
    form = CombinationForm
    search_fields = ['characteristic__title']


admin.site.register(CharacteristicGroup, CharacteristicGroupAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Combination, CombinationAdmin)
