from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    description = models.TextField('Description', default='', blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    is_super = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)