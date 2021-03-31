from django.db import models
from faker import Faker
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def dummy(cls, n):
        f = Faker()
        for _ in range(n):
            cls.objects.create(name=f.name())


    def __str__(self):
        return f'{self.pk}: {self.name}'

    

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='my_articles')
    editor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='edit_articles')

    likes = models.ManyToManyField(Person, related_name='likes') # related name 안쓰면 article_set 겹침.
    scraps = models.ManyToManyField(Person, related_name='scraps')
    dislikes = models.ManyToManyField(Person, related_name='dislikes')
    @classmethod
    def dummy(cls, n):
        f = Faker()
        for _ in range(n):
            cls.objects.create(title=f.address(), content='hello')

    def __str__(self):
        return f'{self.pk}: {self.title}'



    