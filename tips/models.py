from django.db import models
from django.utils import timezone
from expenses.models import Expenses
from django.contrib.auth.models import User


class Tip(models.Model):
    user_token = User.get_session_auth_hash
    author = models.CharField(max_length=32)
    text = models.TextField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

    category = models.CharField(max_length=32, choices=Expenses.Category.choices, default=Expenses.Category.OTHER)

    @staticmethod
    def create_tip(category, author, date, text):
        tip = Tip(category=category, author=author, date=date, text=text)
        tip.save()
        return tip

    def __str__(self):
        preview_tip = self.text[:10] + '...'
        return preview_tip
