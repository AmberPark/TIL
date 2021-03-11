from django.urls import path
from . import views

# practice/
urlpatterns =[
    # practice/'' => 목록 보여주기(전체조회)
    path('', views.index, name="index"),
    # 단일 조회html
    path('<int:pk>/', views.detail, name="detail"),
    # practice/new/ => 새로운 데이터 입력용 html
    path('new/', views.new, name="new"),

    # practice/create/ => 사용자 입력 데이터 처리
    path('create/', views.create, name="create"),
    
    # practice/pk/edit/ => 기존의 데이터를 수정할 HTML
    path('<int:pk>/edit/', views.edit, name='edit'),
    # practice/pk/update/ => 사용자 입력 데이터 처리
    path('<int:pk>/update/', views.update, name='update'),
    # praceice/pk/delete/ => 데이터 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),

]
