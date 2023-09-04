from django import forms
from django.core.validators import RegexValidator


def name_val(value):
    if value[0].islower():
        raise forms.ValidationError('Не с заглавной буквы')
    elif not value.isalpha():
        raise forms.ValidationError('Может содержать только буквы')




class WaterOrder(forms.Form):
    name = forms.CharField(label='Имя', validators=[name_val])
    surname = forms.CharField(label='Фамилия', validators=[name_val])
    email = forms.CharField(label='E-mail')
    phone = forms.CharField(label='Телефон')
    terms = ((1, '1 месяц'), (3, '3 месяца'), (6, '6 месяцев'), (12, '12 месяцев'))
    term = forms.TypedChoiceField(label='Длительность доставки', choices=terms)
    sizes = ((5, '5 литров'), (10, '10 литров'), (15, '15 литров'))
    size = forms.TypedChoiceField(label='Объём баллонов', choices=sizes)