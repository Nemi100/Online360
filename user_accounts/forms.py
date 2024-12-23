# user_accounts/forms.py
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_picture', 'bio', 'linkedin_profile', 'past_works', 'core_language_strength', 'hourly_rate', 'availability', 'consultation_cost']
