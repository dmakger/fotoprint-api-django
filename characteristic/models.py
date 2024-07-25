from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class CharacteristicGroup(models.Model):
    """ГРУППА ХАРАКТЕРИСТИК. Указывает в какой группе находятся характеристики"""
    title = models.CharField('Название', max_length=128, unique=True)

    class Meta:
        verbose_name = "Группа характеристик"
        verbose_name_plural = "Группы характеристик"

    def __str__(self):
        return self.title


class Characteristic(models.Model):
    """ХАРАКТЕРИСТИКИ"""
    characteristic_group = models.ForeignKey(CharacteristicGroup, on_delete=models.CASCADE, verbose_name='Группа')
    title = models.CharField('Название', max_length=128, unique=True)
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"

    def __str__(self):
        return self.title


class Combination(MPTTModel):
    """Комбинация характеристик"""
    characteristic_group = models.ForeignKey(CharacteristicGroup, on_delete=models.CASCADE, verbose_name='Группа')
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, verbose_name='Характеристика')
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Комбинация характеристик"
        verbose_name_plural = "Комбинации характеристик"

    class MPTTMeta:
        order_insertion_by = ['characteristic']

    def __str__(self):
        return self.characteristic.title

