# Generated by Django 4.1 on 2024-03-31 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Статистика продукта',
                'verbose_name_plural': 'Статистики продуктов',
            },
        ),
    ]