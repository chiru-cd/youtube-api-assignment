from django.db import models

# Create your models here.


class Video(models.Model):
    published_at = models.DateTimeField()
    channel_id = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=1024, blank=False)
    channel_title = models.CharField(max_length=255, blank=False)
    video_id = models.CharField(max_length=255, blank=False, unique=True)
    def __str__(self):
        return self.title