from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from .forms import NewUserForm
from .forms import LoginForm
from .models import CustomUser as User

# View for registration
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('voting:index')
        else:
            context = {'errors': form.errors, 'form': form}
            return render(request, 'accounts/register.html', context)
    else:
        form = NewUserForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

# View for login
def login(request):
    return auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=LoginForm)(request)

# View for logout
def logout(request):
    return auth_views.LogoutView.as_view()(request)

# View for profile
@login_required
def profile(Request):
    user = get_object_or_404(User, pk=Request.user.id)
    context = {'user': user}
    return render(Request, 'accounts/profile.html', context)

# View for edit profile
@login_required
def edit_profile(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        else:
            context = {'errors': form.errors, 'form': form}
            return render(request, 'accounts/edit_profile.html', context)
    else:
        form = NewUserForm(instance=user)
        context = {'form': form}
        return render(request, 'accounts/edit_profile.html', context)