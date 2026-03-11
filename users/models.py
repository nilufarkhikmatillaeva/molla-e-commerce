from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name=_('Email')
    )

    phone_number = models.CharField(
        max_length=13,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_('Phone number')
    )

    class Meta:
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email