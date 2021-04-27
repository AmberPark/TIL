from django.shortcuts import get_object_or_404
from rest_framework.response import Response # 이전의 render
from rest_framework.decorators import api_view # 이전의 require_methods
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer  # 이전의 ArticleForm

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
        if serializer.is_valid(raise_exception=True):
            article = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        
    #update
    elif request.method == 'PUT':
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        

    elif request.method == 'DELETE':
        article.delete()
        data = { # customize message
            'success': True,
            'message': f'{article_pk}번 게시물이 삭제되었습니다.',
        }
        return Response(data=data, status=204)

@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def update_or_delete_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        comment.delete()
        data = { # customize message
            'success': True,
            'message': f'{comment_pk}번 댓글이 삭제되었습니다.',
        }
        return Response(data=data, status=204)
