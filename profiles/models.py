from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=30, verbose_name='Имя')
    # last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Email')
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"