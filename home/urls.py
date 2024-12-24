from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard
]
