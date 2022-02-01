from .models import Restoran, Bluda
from django.forms import ModelForm, TextInput, NumberInput, CharField, ModelChoiceField, ImageField, IntegerField, \
    FloatField, Textarea


class RestoranForm(ModelForm):
    class Meta:
        model = Restoran
        fields=['nazvan', 'adres', 'telefon','content','foto']
    widgets={
        'nazvan': TextInput(attrs={'class':'form-control', 'placeholder': 'Название ресторана'}),
        'adres': TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес ресторана'}),
        'telefon': NumberInput (attrs={'class': 'form-control', 'placeholder': 'Телефон в формате 80...', 'step':11 }),
    }

class BludaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kategor'].empty_label = "Категория не выбрана"
    class Meta:
        model = Bluda
        fields=['title', 'kategor', 'foto','full_text','masa','cena','name_restoran']

    widgets = {
        'title': TextInput(attrs={'class':'form-input', 'placeholder': 'Название ресторана'}),
        'full_text': Textarea(attrs={'cols': 170, 'rows':50, 'placeholder': 'Список продуктов'}),
         }

