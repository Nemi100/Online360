from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'review', 'rating', 'timestamp')
    search_fields = ('user__username', 'review', 'rating')
