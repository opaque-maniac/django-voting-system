from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset-done/', views.password_reset_done, name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset-complete/', views.password_reset_complete, name='password_reset_complete'),
    path('password-change/', views.password_change, name='password_change'),
    path('password-change-done/', views.password_change_done, name='password_change_done'),
    path('password-change-confirm/', views.password_change_confirm, name='password_change_confirm'),
    path('password-change-complete/', views.password_change_complete, name='password_change_complete',)
]