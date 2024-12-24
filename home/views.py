from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from reviews.models import Review
from metrics.models import Metric
from jobs.models import Category

def home_view(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            if profile.is_employer:
                return employer_home_view(request)
            else:
                return freelancer_home_view(request)
        except User.profile.RelatedObjectDoesNotExist:
            return render(request, 'home/index.html')
    else:
        return render(request, 'home/index.html')

@login_required
def dashboard_view(request):
    reviews = Review.objects.filter(user=request.user).order_by('-timestamp')[:5]  # User-specific reviews
    metrics = Metric.objects.filter(user=request.user).order_by('deadline')  # User-specific metrics
    return render(request, 'home/dashboard.html', {'reviews': reviews, 'metrics': metrics})

def employer_home_view(request):
    categories = Category.objects.all()
    reviews = Review.objects.all().order_by('-timestamp')[:5]  # Display 5 recent reviews
    return render(request, 'home/employer_home.html', {'categories': categories, 'reviews': reviews})

def freelancer_home_view(request):
    categories = Category.objects.all()
    reviews = Review.objects.filter(user=request.user).order_by('-timestamp')[:5]  # User-specific reviews
    return render(request, 'home/freelancer_home.html', {'categories': categories, 'reviews': reviews})
