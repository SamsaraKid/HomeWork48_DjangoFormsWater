from django import forms
from django.core.validators import RegexValidator

fields = ('Имя:', 'Фамилия:', 'E-mail:', 'Телефон:', 'Длительность:', 'Объём:')


def name_val(value):
    if value[0].islower():
        raise forms.ValidationError('Не с заглавной буквы')
    elif not value.isalpha():
        raise forms.ValidationError('Может содержать только буквы')


class WaterOrder(forms.Form):
    name = forms.CharField(label=fields[0], validators=[name_val])
    surname = forms.CharField(label=fields[1], validators=[name_val])
    email = forms.CharField(label=fields[2])
    phone = forms.CharField(label=fields[3])
    terms = ((1, '1 месяц'), (3, '3 месяца'), (6, '6 месяцев'), (12, '12 месяцев'))
    term = forms.TypedChoiceField(label=fields[4], choices=terms)
    sizes = ((5, '5 литров'), (10, '10 литров'), (15, '15 литров'))
    size = forms.TypedChoiceField(label=fields[5], choices=sizes)