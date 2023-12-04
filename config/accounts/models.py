from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    STATUS = (
        ('regular', 'Regular'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=7, choices=STATUS, default='regular')
    description = models.TextField('Description', default='', blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)