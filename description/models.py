from django.db import models
from django.utils import timezone


class Description(models.Model):
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    # house_id = models.ForeignKey('user_id', on_delete=models.CASCADE)
