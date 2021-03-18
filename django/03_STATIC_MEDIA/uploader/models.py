from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # blank => ORM 이 빈것을 허용함 . DB는 자동으로 ''가 저장됨 => 비어있을 때 , .is_valid() 통과.
    image = ProcessedImageField(
        upload_to='article/',
        blank=True,
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality':90},
    )
    # image = models.ImageField(blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
