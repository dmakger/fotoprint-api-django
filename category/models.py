from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    """Категория"""
    title = models.CharField('Название', max_length=128)
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    def get_full_path(self, sep=' > '):
        path = [self.title]
        k = self.parent
        while k:
            path.append(k.title)
            k = k.parent
        return sep.join(reversed(path))
