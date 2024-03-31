from django.db import models

from category.models import Category
from characteristic.models import CharacteristicItem, GroupCharacteristic, Characteristic


# ОСНОВА ДЛЯ ПРОДУКТОВ. От неё продукты наследуют информацию о продукте
class BaseProduct(models.Model):
    title = models.CharField('Название', max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = "Основа продукта"
        verbose_name_plural = "Основы продуктов"

    def __str__(self):
        return self.title


# ГРУППА ПРОДУКТОВ. Показывает все возможные продукты под
class GroupProduct(models.Model):
    title = models.CharField('Название', max_length=128)
    base = models.ForeignKey(BaseProduct, on_delete=models.CASCADE, verbose_name='Основа продукта')
    number = models.IntegerField('Порядковый номер', default=1)

    class Meta:
        verbose_name = "Группа продукта"
        verbose_name_plural = "Группы продуктов"

    def __str__(self):
        return self.title


# ПРОДУКТ
class Product(models.Model):
    title = models.CharField('Название', max_length=128)
    group = models.ForeignKey(GroupProduct, on_delete=models.CASCADE, verbose_name='Группа продукта')
    image = models.ImageField('Изображение', upload_to='media/product/image/', blank=True, null=True)
    price = models.IntegerField('Стоимость')
    execution_time = models.CharField('Время работы', max_length=32, blank=True, null=True)
    number = models.IntegerField('Порядковый номер', default=1)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


# ХАРАКТЕРИСТИКА ПРОДУКТА
class CharacteristicProduct(models.Model):
    title = models.CharField('Название', max_length=128)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    group_characteristic = models.ForeignKey(GroupCharacteristic, on_delete=models.CASCADE, verbose_name='Группа характеристик')
    number = models.IntegerField('Порядковый номер', default=1)

    class Meta:
        verbose_name = "Характеристика продукта"
        verbose_name_plural = "Характеристики продуктов"

    def __str__(self):
        return f"{self.title}"


# КОНКРЕТНАЯ ХАРАКТЕРИСТИКА ПРОДУКТА
class CharacteristicProductItem(models.Model):
    characteristic_product = models.ForeignKey(CharacteristicProduct, on_delete=models.CASCADE, verbose_name='Характеристика продукта')
    characteristic_item = models.ForeignKey(CharacteristicItem, on_delete=models.CASCADE, verbose_name='Элемент характеристики')
    price = models.IntegerField('Стоимость', default=0)
    number = models.IntegerField('Порядковый номер', default=1)

    class Meta:
        verbose_name = "Характеристика продукта"
        verbose_name_plural = "Характеристики продуктов"

    def __str__(self):
        return f"{self.characteristic_product} - {self.characteristic_item}"

