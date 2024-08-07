# Generated by Django 4.1 on 2024-07-27 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productcharacteristiccombination_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcharacteristiccombination',
            name='title',
            field=models.CharField(blank=True, default=None, help_text='Если не указывать данное поле, то оно наследуется от `product.title`', max_length=128, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='productform',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcharacteristiccombination', verbose_name='Комбинация продуктов'),
        ),
    ]
