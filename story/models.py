from django.db import models
from django.utils import timezone
from house.models import House


class Story(models.Model):
    house_ID = models.ForeignKey(House, on_delete=models.CASCADE)
    last_edited = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def create_story(house_ID, last_edited, text):
        story = Story(house_ID=house_ID, last_edited=last_edited, text=text)
        story.save()
        return story

    def __str__(self):
        return self.text
