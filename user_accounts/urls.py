from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user_accounts/login.html'), name='login'),
    path('profile/create/', views.create_profile, name='profile_create'),
    path('profile/update/', views.update_profile, name='profile_update'),
    path('profile/delete/', views.delete_profile, name='profile_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
]
