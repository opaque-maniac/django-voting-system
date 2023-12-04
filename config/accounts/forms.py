from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django import forms

# Form for registration
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Username"
                }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Username",
                }),
            "password1": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Password",
                }),
            "password2": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
                }),
        }

# Form for login
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Username",
                }),
            'password': forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Password",
                }),
            }
        
# Form for password reset
class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email",
        }))