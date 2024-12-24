from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'profile_picture', 'bio', 'linkedin_profile', 'past_works', 'core_language_strength', 'hourly_rate', 'availability', 'consultation_cost', 'is_employer')
    search_fields = ('user__username', 'first_name', 'last_name', 'bio', 'core_language_strength')
