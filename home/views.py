from django.shortcuts import render
from django.contrib.auth.decorators import login_required  
from reviews.models import Review
from metrics.models import Metric

def home_view(request):
    reviews = Review.objects.all().order_by('-timestamp')[:5]  # Display 5 recent reviews
    return render(request, 'home/home.html', {'reviews': reviews})

@login_required
def dashboard_view(request):
    reviews = Review.objects.filter(user=request.user).order_by('-timestamp')[:5]  # User-specific reviews
    metrics = Metric.objects.filter(user=request.user).order_by('deadline')  # User-specific metrics
    return render(request, 'home/dashboard.html', {'reviews': reviews, 'metrics': metrics})
