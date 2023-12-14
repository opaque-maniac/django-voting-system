from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Profile

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-input email',
            'placeholder': 'Enter your email',
        })
    )
    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.TextInput(attrs={
            'class': 'form-input first-name',
            'placeholder': 'Enter your first name',
        })
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        widget=forms.TextInput(attrs={
            'class': 'form-input last-name',
            'placeholder': 'Enter your last name',
        })
    )
    password1 = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input password1',
            'placeholder': 'Enter password',
        })
    )
    password2 = forms.CharField(
        required=True,
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input password2',
            'placeholder': 'Confirm password',
        })
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
            raise ValidationError("The email already has an account")
        return email

    def save(self):
        user = User.objects.create(
            username = self.cleaned_data['email'],
            email = self.cleaned_data['email'],
            password1 = self.cleaned_data['password1'],
            password2 = self.cleaned_data['password2']
        )
        profile = Profile.objects.create(
            user = user,
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
        )
        return user, profile
    
class LoginForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-input email',
            'placeholder': 'Enter your email',
        })
    )
    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input password1',
            'placeholder': 'Enter password',
        })
    )

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-input email',
            'placeholder': 'Enter your email',
        })
    )
    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.TextInput(attrs={
            'class': 'form-input first-name',
            'placeholder': 'Enter your first name',
        })
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        widget=forms.TextInput(attrs={
            'class': 'form-input last-name',
            'placeholder': 'Enter your last name',
        })
    )
    image = forms.FileField(
        required=False,
        label='Profile Picture',
        widget=forms.FileInput(attrs={
            'class': 'form-input profile-pic',
        })
    )

    def save(self, user_instance):
        user = user_instance
        profile = Profile.objects.get(user=user)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.image = self.cleaned_data['image']
        profile.save()
        user.save()
        return profile, user
