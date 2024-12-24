from django.contrib import admin
from .models import Job, Category

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'description', 'budget', 'due_date', 'category')
    search_fields = ('title', 'employer__username', 'category__name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
