from django import forms

from .models import Vote
from .models import Election
from .models import Candidate
from .models import Party

class NewElectionForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = ('title', 'description', 'start_date', 'end_date',)
        labels = {
            'title': 'Election Title',
            'description': 'Election Description',
            'start_date': 'Election Start Date',
            'end_date': 'Election End Date',
        }
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class NewCandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('name', 'party', 'bio',)
        labels = {
            'name': 'Candidate Name',
            'bio': 'Candidate Bio',
            'party': 'Candidate Party',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Candidate Name'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Candidate Bio'}),
            'party': forms.Select(attrs={'placeholder': 'Candidate Party'}),
        }

class NewPartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ('name', 'description',)
        labels = {
            'name': 'Party Name',
            'description': 'Party Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Party Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Party Description'}),
        }

class NewVoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ('chosen_candidate',)
        labels = {
            'chosen_candidate': 'Chosen Candidate',
        }
        widgets = {
            'chosen_candidate': forms.Select(attrs={'placeholder': 'Chosen Candidate'}),
        }