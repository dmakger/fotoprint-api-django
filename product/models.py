from django.db import models

from category.models import Category
from characteristic.models import Combination, ExecutionTime


class Product(models.Model):
    """ПРОДУКТ"""
    title = models.CharField('Название', max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField('Изображение', upload_to='product/image/', blank=True, null=True)

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
    # percent = models.FloatField('Процент', default=0.)

    class Meta:
        verbose_name = "Дополнительная услуга у продукта"
        verbose_name_plural = "Дополнительные услуги у продуктов"

    def __str__(self):
        return self.title


# ======{ КОМБИНАЦИЯ ХАРАКТЕРИСТИК }======
class ProductCharacteristicCombination(models.Model):
    """Комбинации характеристик у продукта"""
    title = models.CharField('Название', max_length=128, default=None, blank=True, null=True,
                             help_text="Если не указывать данное поле, то оно наследуется от `product.title`")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    combination = models.ForeignKey(Combination, on_delete=models.CASCADE, verbose_name='Комбинация')
    price = models.FloatField('Стоимость', default=0.)
    image = models.ImageField('Изображение', upload_to='productCombination/image/', blank=True, null=True)
    show_as_product = models.BooleanField("Отображать как продукт", default=True)
    execution_time = models.ForeignKey(ExecutionTime, on_delete=models.CASCADE, verbose_name='Срок исполнения', blank=True, null=True)

    class Meta:
        verbose_name = "Комбинация характеристик у продукта"
        verbose_name_plural = "Комбинации характеристик у продукта"

    def __str__(self):
        return self.get_title()

    def get_title(self):
        if self.title:
            return self.title
        return self.product.title

    def get_image(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        if self.product.image and hasattr(self.product.image, 'url'):
            return self.product.image.url
        return None


    def save(self, *args, **kwargs):
        if not self.title:
            self.title = f"{self.product.title}: {self.combination.characteristic.title}"
        super().save(*args, **kwargs)


# ======{ ФОРМЫ }======
class ProductForm(models.Model):
    """Форма продукта"""
    product = models.ForeignKey(ProductCharacteristicCombination, on_delete=models.CASCADE,
                                verbose_name='Комбинация продуктов')
    title = models.CharField('Название', max_length=128)
    title_admin = models.CharField('Название для админки', max_length=128, blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Форма продукта"
        verbose_name_plural = "Формы продуктов"

    def __str__(self):
        return self.title_admin

    def save(self, *args, **kwargs):
        if not self.title_admin:
            self.title_admin = self.title
        super().save(*args, **kwargs)


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
