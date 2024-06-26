# Generated by Django 4.1 on 2024-03-31 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('characteristic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Основа продукта',
                'verbose_name_plural': 'Основы продуктов',
            },
        ),
        migrations.CreateModel(
            name='CharacteristicProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('number', models.IntegerField(default=1, verbose_name='Порядковый номер')),
                ('group_characteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characteristic.groupcharacteristic', verbose_name='Группа характеристик')),
            ],
            options={
                'verbose_name': 'Характеристика продукта',
                'verbose_name_plural': 'Характеристики продуктов',
            },
        ),
        migrations.CreateModel(
            name='GroupProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('number', models.IntegerField(default=1, verbose_name='Порядковый номер')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.baseproduct', verbose_name='Основа продукта')),
            ],
            options={
                'verbose_name': 'Группа продукта',
                'verbose_name_plural': 'Группы продуктов',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/product/image/', verbose_name='Изображение')),
                ('price', models.FloatField(verbose_name='Стоимость')),
                ('execution_time', models.CharField(blank=True, max_length=32, null=True, verbose_name='Время работы')),
                ('number', models.IntegerField(default=1, verbose_name='Порядковый номер')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.groupproduct', verbose_name='Группа продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='CharacteristicProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0, verbose_name='Стоимость')),
                ('number', models.IntegerField(default=1, verbose_name='Порядковый номер')),
                ('characteristic_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characteristic.characteristicitem', verbose_name='Элемент характеристики')),
                ('characteristic_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.characteristicproduct', verbose_name='Характеристика продукта')),
            ],
            options={
                'verbose_name': 'Конкретная характеристика продукта',
                'verbose_name_plural': 'Конкретные характеристики продуктов',
            },
        ),
        migrations.AddField(
            model_name='characteristicproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Продукт'),
        ),
    ]
