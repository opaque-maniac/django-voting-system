from django.db import models
from django.utils import timezone

from accounts.models import Profile

# Create your models here.
class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='candidate_images/', blank=True, null=True)
    party = models.ForeignKey('Party', on_delete=models.CASCADE)
    election = models.ForeignKey('Election', on_delete=models.CASCADE)
    vote_count = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = 'candidate'
        verbose_name_plural = 'candidates'
     
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Party(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='party_images/', blank=True, null=True)

    class Meta:
        verbose_name = 'party'
        verbose_name_plural = 'parties'
     
    def __str__(self):
        return f"{self.name}"

class Election(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    has_ended = models.BooleanField(default=False)
    vote_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'election'
        verbose_name_plural = 'elections'
     
    def __str__(self):
        return f"{self.name}"

class Vote(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    election = models.ForeignKey('Election', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'vote'
        verbose_name_plural = 'votes'
     
    def __str__(self):
        return f"{self.candidate} - {self.election} - {self.user}"