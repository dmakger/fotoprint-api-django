from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from category.models import Category


#  КАТЕГОРИЯ
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


admin.site.register(Category, DraggableMPTTAdmin)
