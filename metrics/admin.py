from django.contrib import admin
from .models import Metric

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_name', 'milestone', 'deadline', 'status', 'timestamp')
    search_fields = ('user__username', 'project_name', 'milestone', 'status')
