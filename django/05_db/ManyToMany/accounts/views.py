from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

def follow(request, username):
    star = get_object_or_404(User, username=username)
    fan = request.user
    if request.user.is_authenticated:
        if fan != star:
            if fan.stars.filter(pk=star.pk).exists():
                fan.stars.remove(star)
            else:
                fan.stars.add(star)
    return
