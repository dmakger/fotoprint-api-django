# Generated by Django 4.1 on 2024-07-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_productform_title_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productform',
            name='title_admin',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Название для админки'),
        ),
    ]
