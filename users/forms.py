from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=30,
        required=True
    )
    email = forms.EmailField(
        label='Email',
        required=True
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        help_text='Формат: +79991234567'
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput,
        help_text='Введите пароль ещё раз для проверки'
    )

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

class LoginForm(forms.Form):
    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )