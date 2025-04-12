from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import Customer
import re


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'autofocus': True}),
        validators=[RegexValidator(
            regex='^[а-яА-ЯёЁ\- ]+$',
            message='Имя может содержать только русские буквы, дефисы и пробелы'
        )]
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=30,
        required=True,
        validators=[RegexValidator(
            regex='^[а-яА-ЯёЁ\- ]+$',
            message='Фамилия может содержать только русские буквы, дефисы и пробелы'
        )]
    )
    email = forms.EmailField(
        label='Email',
        required=True
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        help_text='Формат: +79001234567',
        validators=[RegexValidator(
            regex='^\+79\d{9}$',
            message='Телефон должен быть в формате +79001234567'
        )]
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        help_text='Минимум 5 символов, только латинские буквы и цифры',
        validators=[RegexValidator(
            regex='^[a-zA-Z0-9]+$',
            message='Пароль может содержать только латинские буквы и цифры'
        )]
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput,
        help_text='Введите пароль ещё раз для проверки'
    )

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Отключаем стандартные сообщения об ошибках
        self.fields['password1'].help_text = 'Минимум 5 символов, только латинские буквы и цифры'
        self.fields['password2'].help_text = 'Введите пароль ещё раз для проверки'

        # Убираем стандартные валидаторы
        self.fields['password1'].validators = [
            RegexValidator(
                regex='^[a-zA-Z0-9]+$',
                message='Пароль может содержать только латинские буквы и цифры'
            )
        ]

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 5:
            raise ValidationError('Пароль должен содержать не менее 5 символов')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['phone']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'placeholder': '+79001234567'
        }),
        validators=[RegexValidator(
            regex='^\+79\d{9}$',
            message='Телефон должен быть в формате +79001234567'
        )]
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите ваш пароль'
        }),
        validators=[RegexValidator(
            regex='^[a-zA-Z0-9]+$',
            message='Пароль может содержать только латинские буквы и цифры'
        )]
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not Customer.objects.filter(phone=phone).exists():
            raise ValidationError('Пользователь с таким номером телефона не найден')
        return phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 5:
            raise ValidationError('Пароль должен содержать не менее 5 символов')
        return password