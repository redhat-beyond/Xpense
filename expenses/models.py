from django.db import models
from django.utils import timezone


class Expenses(models.Model):
    # house_id = models.ForeignKey('user_id', on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(timezone.now())

    class Category(models.TextChoices):
        RENT = 'Rent'
        MORTGAGE = 'Mortgage'
        BILLS = 'bills'
        TRANSPORTATION = 'Transportation'
        CLOTHING = 'Clothing'
        HEALTHCARE = 'Healthcare'
        FOOD = 'Food'
        INSURANCE = 'Insurance'
        KIDS = 'Kids'
        CULTURE = 'Culture'
        VACATIONS = 'Vacations'
        OTHER = 'Other'

    category = models.CharField(
        max_length=32,
        choices=Category.choices,
        default=Category.OTHER
    )

    def __str__(self):
        return f'Category:{self.category},Amount:{self.amount}'

    def recent(self):
        pass
        # returns if the model is from the last 3 month
        return self.category
