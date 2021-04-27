from django import forms
from rest_framework import serializers
from .models import Article, Comment

# serializer의 존재이유
# 1. 데이터 검증
# 2.HTML 생성
# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = '__all__'

# 1. 데이터 검증
# 2. JSON 생성
# comment 관련 JSON 담당자
class CommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField(min_length=1, max_length=200)
 
    class Meta:
        model = Comment
        fields = '__all__' # JSON에는 모든 필드가 포함되고
        # exclude = ('article',)
        read_only_fields = ('article',) # CUD관련 validation 은 포함하지 않는다.

class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=2, max_length=100)
    content = serializers.CharField(min_length=2)
    # Comment 관련한 json도 포함해야함 => CommentSerializer가 들어가야 한다
    # related_name 과 동일하게 작성
    comments = CommentSerializer(many=True, read_only=True) # read_only => 수정 x
    class Meta:
        model = Article
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):
    # 댓글 개수 확인 => 댓글 JSON 담당자 소환
    comments = CommentSerializer(many=True)
    # 없는 필드를 (댓글 개수)를 만들어서 json을 구성하자
    comment_count = serializers.IntegerField(source='comments.count')
    class Meta:
        model = Article
        fields = ('pk', 'title', 'comments', 'comment_count',)
        read_only_fields = fields
        # read_only 속성 == read_only_fields 에 쓰는거랑 같음

