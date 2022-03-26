from django.db import models


class Expenses(models.Model):
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
        OTHER = 'Other2'

    category = models.CharField(
        max_length=32,
        choices=Category.choices,
        default=Category.OTHER
    )

    def __str__(self):
        return self.category
