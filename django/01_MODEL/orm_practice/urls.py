from django.urls import path
from . import views

# practice/
urlpatterns =[
    path('', views.index, name="index"),
    # practice/'' => 목록 보여주기(전체조회)
    path('<int:pk>', views.detail, name="detail"),
    # practice/new/ => 새로운 데이터 입력용 html
    path('new/', views.new, name="new"),

    # practice/create/ => 사용자 입력 데이터 처리
    path('create/', views.create, name="create"),
    
]
