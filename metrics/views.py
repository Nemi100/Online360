from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Metric

@login_required
def metric_dashboard(request):
    metrics = Metric.objects.filter(user=request.user).order_by('deadline')
    return render(request, 'metrics/dashboard.html', {'metrics': metrics})
