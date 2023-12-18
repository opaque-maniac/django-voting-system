from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from . import forms
from .models import Profile

# View for the register page
def register_view(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = authenticate(username=email, password=password)
                login(request, user)
                messages.success(request, "Registered successfully!")
                return redirect('voting:index')
            except ValidationError as e:
                form.add_error(e.messages[0])
                context = { 'form': form, 'errors': form.errors }
    else:
        context = { 'form': forms.RegisterForm() }
    return render(request, 'accounts/register.html', context)

# View for the login page
def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(username=email, password=password)
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('voting:index')
            except ValidationError as e:
                form.add_error(e.messages[0])
                context = { 'form': form, 'errors': form.errors }
    else:
        context = { 'form': forms.LoginForm() }
    return render(request, 'accounts/login.html', context)

# View for the login page
def logout_view(request):
    logout(request)
    return redirect('voting:index')

# View for the profile page
@login_required
def profile(request):
    user = User.objects.get(pk=request.user.pk)
    profile = Profile.objects.get(user=user)
    context = { 'user': user, 'profile': profile }
    return render(request, 'accounts/profile.html', context)

@login_required
def update_profile(request):
    user = User.objects.get(pk=request.user.pk)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        form =forms.ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('account:profile')
        else:
            form.add_error("Error occured when updating profile")
            context = { 'form': form, 'errors': form.errors }
    else:
        initial_data = {
            'email': user.email,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'image': profile.image.url if profile.image else None
        }
        form = forms.ProfileForm(initial=initial_data)
        context = { 'form': form }
    return render(request, 'account/edit_profile.html', context)
