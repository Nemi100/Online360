from django.db import models
from django.contrib.auth.models import User
from jobs.models import Category

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    past_works = models.TextField(blank=True, null=True)
    core_language_strength = models.CharField(max_length=100, blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    availability = models.CharField(max_length=100, blank=True, null=True)
    consultation_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    is_employer = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
