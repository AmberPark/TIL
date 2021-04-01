from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
# ... 

def like(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    if user.is_authenticated:
        if article.like_users.filter(pk=user.pk).exists():
            article.like_user.remove(user)
        else:
            article.like_users.add(user)
    return redirect('insta:index', article.pk)

