from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return HttpResponse('This is asrticles/index')

def mail(request):
    return HttpResponse('96amber@naver.com')
