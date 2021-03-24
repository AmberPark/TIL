from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# from .models import User
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.decorators.http import require_GET, require_POST, require_http_methods


User = get_user_model()

@login_required
def profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save()
            return redirect('accounts:profile', username=user_profile.username)
    else:
        form = CustomUserChangeForm(instance=user_profile)
 
    context = {
        'user_profile': user_profile,
        'form':form,
    }
    return render(request, 'accounts/profile.html', context)

# @require_GET
# def index(request):
#     users = User.objects.all()
#     context = {'users':users, }
#     return render(request, 'accounts/index.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, form.user)
            form.save()
            return redirect('accounts:profile', request.user.username)   

    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form,}
    return render(request, 'accounts/change_password.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인을 시켜야하는데,,,
            # 세션 create
            auth_login(request, form.get_user())
            # 로그인 안한 상태에서 create 눌렀을때 login 페이지로 오고 로그인 하고 나면 바로 글 쓰는 페이지록 가도록
            next_url = request.GET.get('next')        
            # none이 나올수가 있는거를 or 앞에 둬야함
            return redirect(next_url or 'articles:index')
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
            return redirect('accounts:profile', user.username)
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required
@require_POST
def withdraw(request):
    user = request.user.delete()
    auth_logout(request)
    return redirect('articles:index')
    