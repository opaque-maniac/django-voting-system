from django.db import models
from django.contrib.auth.models import User

# Model for elections
class Election(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
# Model for party
class Party(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Model for candidate
class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.name

# Model for vote
class Vote(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, related_name='voter', on_delete=models.CASCADE)
    chosen_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.voter_name} voted for {self.chosen_candidate} in {self.election}"
