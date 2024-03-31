from django.contrib import admin

#  КАТЕГОРИЯ
from mptt.admin import DraggableMPTTAdmin

from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


admin.site.register(Category, DraggableMPTTAdmin)
# admin.site.register(Category, CategoryAdmin)
