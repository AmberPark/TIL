from django.db import models

# Create your models here.
class Article(models.Model):
    # ORM 은 models.py 내부 class 에서 class var 만 확인해 DB의 column으로 만든다. 밑에 method 만들어도 migrations 파일에 영향 x
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} => {self.title}'