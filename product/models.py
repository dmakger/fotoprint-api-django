from django.db import models

from category.models import Category
from characteristic.models import CharacteristicItem, GroupCharacteristic


# ПРОДУКТ
class Product(models.Model):
    title = models.CharField('Название', max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField('Изображение', upload_to='product/images/', null=True, default=None, blank=True)
    execution_time = models.CharField('Количество рабочих дней', max_length=128, null=True, default=None, blank=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


# ПРОДУКТ к ЭЛЕМЕНТУ ХАРАКТЕРИСТИК
class ProductToCharacteristicItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Проект')
    characteristic_item = models.ForeignKey(CharacteristicItem, on_delete=models.CASCADE,
                                            verbose_name='Элемент характеристик')
    group_characteristic = models.ForeignKey(GroupCharacteristic, on_delete=models.CASCADE, verbose_name='Проект')
    price = models.FloatField('Стоимость', default=0)
    number = models.IntegerField('Порядковый номер', default=1)

    class Meta:
        verbose_name = "Продукт к Характеристикам"
        verbose_name_plural = "Продукты к Характеристикам"

    def __str__(self):
        return f"{self.product} {self.characteristic_item}"
