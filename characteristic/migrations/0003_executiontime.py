# Generated by Django 4.1 on 2024-07-25 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characteristic', '0002_alter_characteristic_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutionTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Срок исполнения',
                'verbose_name_plural': 'Сроки исполнения',
            },
        ),
    ]