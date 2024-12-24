from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.metric_dashboard, name='metric_dashboard'),
]
