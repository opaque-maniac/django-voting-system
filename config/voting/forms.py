from django import forms
from . import models

# Form for the new election
class ElectionForm(forms.ModelForm):
    class Meta:
        model = models.Election
        fields = ['name', 'description', 'start_date', 'end_date']
        widget = {
            'name': forms.TextInput(attrs={
                'class': 'form-input name',
                'placeholder': 'Enter election name',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-input description',
                'placeholder': 'Enter election description',
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-input start-date',
                'placeholder': 'Enter start date',
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-input end-date',
                'placeholder': 'Enter end date',
            }),
        }

# Form for the new candidate
class CandidateForm(forms.ModelForm):
    class Meta:
        model = models.Candidate
        fields = ['first_name', 'last_name', 'image', 'party']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-input first-name',
                'placeholder': 'Enter first name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input last-name',
                'placeholder': 'Enter last name',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-input image',
                'placeholder': 'Upload image',
            }),
            'party': forms.Select(attrs={
                'class': 'form-input party',
                'placeholder': 'Select party',
            }),
        }

# Form for the new party
class PartyForm(forms.ModelForm):
    class Meta:
        model = models.Party
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input name',
                'placeholder': 'Enter party name',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-input image',
                'placeholder': 'Upload image',
            }),
        }

# Form for new party
class PartyForm(forms.ModelForm):
    class Meta:
        model = models.Party
        fields = ['name', 'image']
        widget = {
            'name': forms.TextInput(attrs={
                'label': 'Party Name',
                'class': 'form-input name',
                'placeholder': 'Enter party name',
            }),
            'image': forms.FileInput(attrs={
                'label': 'Party Image',
                'class': 'form-input image',
                'placeholder': 'Upload image',
            }),
        }