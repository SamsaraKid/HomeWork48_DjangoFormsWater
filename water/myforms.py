from django import forms
from django.core.validators import RegexValidator

fields = ('Имя:', 'Фамилия:', 'E-mail:', 'Телефон:', 'Длительность:', 'Объём:')


def name_val(value):
    if value[0].islower():
        raise forms.ValidationError('Не с заглавной буквы')
    elif not value.isalpha():
        raise forms.ValidationError('Может содержать только буквы')


class WaterOrder(forms.Form):
    name = forms.CharField(label=fields[0], validators=[name_val], initial='Иван')
    surname = forms.CharField(label=fields[1], validators=[name_val], initial='Иванов')
    email = forms.CharField(label=fields[2], validators=[RegexValidator('[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+', message='Некорректный адрес')])
    phone = forms.CharField(label=fields[3], validators=[RegexValidator('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', message='Некорректный телефон')])
    terms = (('1 месяц', '1 месяц'), ('3 месяца', '3 месяца'), ('6 месяцев', '6 месяцев'), ('12 месяцев', '12 месяцев'))
    term = forms.ChoiceField(label=fields[4], choices=terms)
    sizes = (('5 литров', '5 литров'), ('10 литров', '10 литров'), ('15 литров', '15 литров'))
    size = forms.ChoiceField(label=fields[5], choices=sizes)