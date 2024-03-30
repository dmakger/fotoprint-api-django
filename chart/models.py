from django.db import models
from product.models import Product


# СТАТИСТИКА ПРОДУКТА
class ChartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    count_views = models.IntegerField('Количество просмотров', default=0)

    class Meta:
        verbose_name = "Статистика продукта"
        verbose_name_plural = "Статистики продуктов"

    def __str__(self):
        return self.product
