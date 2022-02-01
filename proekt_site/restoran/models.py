from django.db import models


class Bluda(models.Model):
    title = models.CharField('Название', max_length=50)
    kategor = models.ForeignKey('Kategor', on_delete=models.PROTECT)
    foto= models.ImageField('Фото блюда', upload_to='img/')
    full_text=models.TextField('Полный состав')
    masa= models.IntegerField('Вес')
    cena=models.FloatField('Цена в рублях')
    name_restoran= models.ForeignKey('Restoran', on_delete=models.CASCADE)

    class Meta:
        verbose_name='Блюдо'
        verbose_name_plural='Блюда'
    def __str__(self):
        return self.full_text

class Restoran(models.Model):
    nazvan=models.CharField('Название ресторана', max_length=30)
    adres=models.CharField('Адрес', max_length=50)
    telefon=models.IntegerField('Телефон')
    content = models.TextField(blank=True, verbose_name="Описание рестрана")
    foto = models.ImageField('Фото ресторана', upload_to='photo/')


    def __str__(self):
        return self.nazvan

    class Meta:
        verbose_name='Ресторан'
        verbose_name_plural='Рестораны'


class Kategor(models.Model):
    VIBOR_KATEGOR = (
        ('1', 'Закуска'),
        ('2', 'Основное'),
        ('3', 'Десерт'),
        ('4', 'Напиток'),
        ('5', 'Суп'),
    )
    name = models.CharField(max_length=60)
    vibor_kategor = models.CharField(max_length=1, choices=VIBOR_KATEGOR)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

