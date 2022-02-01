# Generated by Django 4.0 on 2022-01-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoran', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bluda',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AlterModelOptions(
            name='kategor',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='restoran',
            options={'verbose_name': 'Ресторан', 'verbose_name_plural': 'Рестораны'},
        ),
        migrations.AlterField(
            model_name='bluda',
            name='foto',
            field=models.ImageField(upload_to='img/', verbose_name='Фото блюда'),
        ),
    ]
