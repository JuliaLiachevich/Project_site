# Generated by Django 4.0 on 2022-01-21 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoran', '0003_restoran_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='restoran',
            name='foto',
            field=models.ImageField(default=2, upload_to='photo/', verbose_name='Фото ресторана'),
            preserve_default=False,
        ),
    ]