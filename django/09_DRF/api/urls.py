from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # path('create/', views.create_article),
    path('articles/', views.article_list_or_create),
    # path('', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail_or_update_or_delete),

    path('articles/<int:article_pk>/comments/', views.create_comment),
    path('articles/<int:article_pk>/comments/<comment_pk>/', views.update_or_delete_comment),
    
]
