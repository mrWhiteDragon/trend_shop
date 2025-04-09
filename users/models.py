from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(AbstractUser):
    phone = models.CharField(
        _('Телефон'),
        max_length=20,
        unique=True,
        help_text=_('Формат: +79991234567')
    )

    class Meta:
        verbose_name = _('Покупатель')
        verbose_name_plural = _('Покупатели')
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.get_full_name()} ({self.phone})"
