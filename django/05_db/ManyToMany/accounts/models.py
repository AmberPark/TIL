from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    # fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')

    # 밑에 두개 같은 코드
    # fans = models.ManyToManyField('self', symmetric=False, related_name='stars')
    stars = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='fans')
    
    # friends = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return f'{self.pk} : {self.username}'
    
    