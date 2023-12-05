from django import forms

from . import models

# Form for creating a new election
class ElectionForm(forms.ModelForm):
    class Meta:
        model = models.Election
        fields = ['title', 'description', 'start_date', 'end_date']

# Form for creating a new candidate
class CandidateForm(forms.ModelForm):
    class Meta:
        model = models.Candidate
        fields = ['election', 'image', 'name', 'bio', 'party']

# Form for creating a new pary
class PatyForm(forms.ModelForm):
    class Meta:
        model = models.Party
        fields = ['election', 'image', 'name', 'description']

# Form for voting
class VotingForm(forms.ModelForm):
    class Meta:
        model = models.Party
        fields = ['chosen_candidate']