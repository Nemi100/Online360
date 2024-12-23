from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_job, name='job_create'),
    path('update/<int:job_id>/', views.update_job, name='job_update'),
    path('delete/<int:job_id>/', views.delete_job, name='job_delete'),
]
