from django.urls import path
from . import views

urlpatterns = [
    # var_route
    path('test/<value>/', views.test),
    
    # 입력받고 처리결과 보여주기 
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]
