from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_message, name='message_send'),
    path('inbox/', views.inbox, name='message_inbox'),
]
