from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user_accounts/register.html', {'form': form})

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    else:
        form = ProfileForm()
    return render(request, 'user_accounts/profile_form.html', {'form': form})

@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'user_accounts/profile_form.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.profile.delete()
        request.user.delete()
        return redirect('home')
    return render(request, 'user_accounts/profile_confirm_delete.html')

@login_required
def dashboard(request):
    return render(request, 'user_accounts/dashboard.html')

def home(request):
    return render(request, 'user_accounts/home.html')

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'user_accounts/profile.html', {'user': user, 'profile': profile})
