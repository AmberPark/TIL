from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username, password, is_actice, is_staff 등 이미 정보들 많음 거기에 추가로 더 쓰겠다를 밑에
    address = models.CharField(max_length=100)

