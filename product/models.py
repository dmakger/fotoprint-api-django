from django.db import models

from category.models import Category
from characteristic.models import Combination, ExecutionTime


class Product(models.Model):
    """ПРОДУКТ"""
    title = models.CharField('Название', max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField('Изображение', upload_to='media/product/image/', blank=True, null=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


# ======{ ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ }======
class ProductAdditionalService(models.Model):
    """Дополнительные услуги у продуктов"""
    title = models.CharField('Название', max_length=128)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    price = models.FloatField('Стоимость', default=0.)

    class Meta:
        verbose_name = "Дополнительная услуга у продукта"
        verbose_name_plural = "Дополнительные услуги у продуктов"

    def __str__(self):
        return self.title


# ======{ КОМБИНАЦИЯ ХАРАКТЕРИСТИК }======
class ProductCharacteristicCombination(models.Model):
    """Комбинации характеристик у продукта"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    combination = models.ForeignKey(Combination, on_delete=models.CASCADE, verbose_name='Комбинация')
    price = models.FloatField('Стоимость', default=0.)
    execution_time = models.ForeignKey(ExecutionTime, on_delete=models.CASCADE, verbose_name='Срок исполнения', blank=True, null=True)

    class Meta:
        verbose_name = "Комбинация характеристик у продукта"
        verbose_name_plural = "Комбинации характеристик у продукта"

    def __str__(self):
        return self.product.title


# ======{ ФОРМЫ }======
class ProductForm(models.Model):
    """Форма продукта"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField('Название', max_length=128)

    class Meta:
        verbose_name = "Форма продукта"
        verbose_name_plural = "Формы продуктов"

    def __str__(self):
        return self.title


class ProductFormCombination(models.Model):
    """Форма продукта"""
    product_form = models.ForeignKey(ProductForm, on_delete=models.CASCADE, verbose_name='Форма продукта')
    combination = models.ForeignKey(Combination, on_delete=models.CASCADE, verbose_name='Комбинация')
    execution_time = models.ForeignKey(ExecutionTime, on_delete=models.CASCADE, verbose_name='Срок исполнения', blank=True, null=True)

    class Meta:
        verbose_name = "Комбинация для формы продукта"
        verbose_name_plural = "Комбинации для форм продуктов"

    def __str__(self):
        return self.product_form.title
