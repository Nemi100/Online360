from django.db import models
from django.contrib.auth.models import User

class Metric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    milestone = models.CharField(max_length=200)
    deadline = models.DateField()
    status = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Metric for {self.user.username} - {self.project_name}'
