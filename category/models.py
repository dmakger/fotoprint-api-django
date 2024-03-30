from django.db import models


# КАТЕГОРИЯ.
class Category(models.Model):
    title = models.CharField('Название', max_length=128)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title
