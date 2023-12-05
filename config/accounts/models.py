from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email