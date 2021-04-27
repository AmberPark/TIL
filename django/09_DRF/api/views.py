from django.shortcuts import get_object_or_404
from rest_framework.response import Response # 이전의 render
from rest_framework.decorators import api_view # 이전의 require_methods
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer  # 이전의 ArticleForm

@api_view(['GET', 'POST'])
def article_list_or_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # 여러개니까 LIST
        serializer = ArticleListSerializer(articles, many=True) # 쿼리셋이면 many=True 필수
        return Response(serializer.data)
    elif request.method == 'POST':
        # print('JSON DATA:', request.data) 
        # request.POST => POST요청 and HTML FormData로 넘어온 데이터만 취급
        # request.GET => URL parmas
        # request.data => 사용자가 제출한 JSON 데이터는 여기에!

        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            article = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    # 여러개니까 LIST
    serializer = ArticleListSerializer(articles, many=True) # 쿼리셋이면 many=True 필수
    return Response(serializer.data)
"""

@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        
    elif request.method == 'PATCH' or request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=204)

"""
@api_view(['POST'])
def create_article(request):
    # print('JSON DATA:', request.data) 
    # request.POST => POST요청 and HTML FormData로 넘어온 데이터만 취급
    # request.GET => URL parmas
    # request.data => 사용자가 제출한 JSON 데이터는 여기에!

    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        article = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""