from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username, password, is_actice, is_staff 등 이미 정보들 많음 거기에 추가로 더 쓰고싶으면 적기.
    address = models.CharField(max_length=100)

