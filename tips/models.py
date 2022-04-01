from django.db import models
from django.utils import timezone
from expenses.models import Expenses


class Tip(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    category = models.CharField(
         max_length=32,
         choices=Expenses.Category.choices,
         default=Expenses.Category.OTHER
    )

    def __str__(self):
        return self.category
