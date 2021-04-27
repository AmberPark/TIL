from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # path('create/', views.create_article),
    path('articles/', views.article_list_or_create),
    # path('', views.article_list),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
]
