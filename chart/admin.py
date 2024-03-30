from django.contrib import admin
from chart.models import ChartProduct


# СТАТИСТИКА ПРОДУКТА
class ChartProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'count_views', 'id']


admin.site.register(ChartProduct, ChartProductAdmin)
