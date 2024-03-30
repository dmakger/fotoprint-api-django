from django.db import models


# ГРУППА ХАРАКТЕРИСТИК. Указывает в какой группе находятся характеристики
class GroupCharacteristic(models.Model):
    title = models.CharField('Название', max_length=128)
    number = models.IntegerField('Порядковый номер', default=1)

    class Meta:
        verbose_name = "Группа характеристик"
        verbose_name_plural = "Группы характеристик"

    def __str__(self):
        return self.title


# ХАРАКТЕРИСТИКИ
class Characteristic(models.Model):
    title = models.CharField('Название', max_length=128)

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"

    def __str__(self):
        return self.title


# ЭЛЕМЕНТЫ ХАРАКТЕРИСТИК.
class CharacteristicItem(models.Model):
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, verbose_name='Характеристика')
    title = models.CharField('Название', max_length=128)
    price = models.FloatField('Стоимость', default=0)

    class Meta:
        verbose_name = "Элемент характеристики"
        verbose_name_plural = "Элементы характеристики"

    def __str__(self):
        return self.title
