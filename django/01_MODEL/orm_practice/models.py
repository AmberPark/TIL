from django.db import models

# Create your models here.
class Student(models.Model): # 테이블 한줄 의 이름(단수형)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    hobby = models.TextField()
