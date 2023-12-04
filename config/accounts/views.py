from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .forms import NewUserForm
from .forms import LoginForm
from .forms import PasswordResetForm

# View for registration
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('voting:index')
        else:
            context = {"error": form.errors, 'form': form }
            return render(request, 'registration/register.html', context)
    else:
        form = NewUserForm()
        context = {"form": form}
        return render(request, 'registration/register.html', context)

# View for login
def login(request):
    return auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm)(request)

# View for logout
def logout(request):
    return auth_views.LogoutView.as_view()(request)

# View for the profile
def profile(request):
    user = get_object_or_404(User, pk=request.user.id)
    context = {"user": user}
    return render(request, 'registration/profile.html', context)

# View for password reset
def password_reset(request):
    return auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html", form_class=PasswordResetForm)(request)

# View for password reset done
def password_reset_done(request):
    return auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html")(request)

# View for password reset confirm
def password_reset_confirm(request, uidb64, token):
    return auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html")(request, uidb64=uidb64, token=token)

# View for password reset complete
def password_reset_complete(request):
    return auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html")(request)

# View for password change
def password_change(request):
    return auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html")(request)

# View for password change done
def password_change_done(request):
    return auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html")(request)

# View for password change confirm
def password_change_confirm(request):
    return auth_views.PasswordChangeConfirmView.as_view(template_name="registration/password_change_confirm.html")(request)

# View for password change complete
def password_change_complete(request):
    return auth_views.PasswordChangeCompleteView.as_view(template_name="registration/password_change_complete.html")(request)