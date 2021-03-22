from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# from .models import User
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_GET, require_POST, require_http_methods


User = get_user_model()
@require_GET
def index(request):
    users = User.objects.all()
    context = {'users':users, }
    return render(request, 'accounts/index.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인을 시켜야하는데,,,
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)
            
@require_http_methods(['GET', 'POST'])
def signup(request):
    # login 한 사용자라면,
    if request.user.is_authenticated:
        return redirect('accounts:index')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 사인업하고 로그인까지
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
    