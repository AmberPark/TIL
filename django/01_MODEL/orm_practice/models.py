from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model): # 테이블 한줄 의 이름(단수형)
    name = models.CharField(max_length=5)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    hobby = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
