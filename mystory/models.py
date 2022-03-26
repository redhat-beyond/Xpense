from django.db import models
from django.utils import timezone
from house.models import House


class MyStory(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    story_date = models.DateTimeField(default=timezone.now)
    story_text = models.TextField()

    def __str__(self):
        return self.story_text
