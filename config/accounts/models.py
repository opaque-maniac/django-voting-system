from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
