from django.db import models

# Create your models here.

# This model holds all the videos objects
class Video(models.Model):

    def __str__(self):
        return self.video_name

    video_name = models.CharField(max_length=500)
    video_url = models.CharField(max_length=500)
