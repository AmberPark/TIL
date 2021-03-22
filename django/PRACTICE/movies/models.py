from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail, ResizeToFill
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    image = ProcessedImageField(
        upload_to='movies/',
        blank=True,
        processors=[Thumbnail(100,200)],
        format='JPEG',
        options={'quality':100},
    )

