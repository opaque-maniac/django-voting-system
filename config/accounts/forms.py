from config.settings import AUTH_USER_MODEL as User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django import forms

# Form for registration
class NewUserForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['email','firstname', 'lastname', 'password1', 'password2', 'profile_picture']
        widgets = {
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Username",
                }),
            "firstname": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name",
                }),
            "lastname": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name",
                }),
            "password1": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Password",
                }),
            "password2": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
                }),
            "profile_picture": forms.FileInput(attrs={
                "class": "form-control",
                "placeholder": "Profile Picture",
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