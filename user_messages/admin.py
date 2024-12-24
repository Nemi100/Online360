from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'timestamp', 'attachment')
    search_fields = ('sender__username', 'receiver__username', 'subject')
