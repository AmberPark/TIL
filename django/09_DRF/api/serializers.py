from django import forms
from rest_framework import serializers
from .models import Article

# serializer의 존재이유
# 1. 데이터 검증
# 2.HTML 생성
# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = '__all__'

# 1. 데이터 검증
# 2. JSON 생성
class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=2, max_length=100)
    class Meta:
        model = Article
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('pk', 'title',)