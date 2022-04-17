from django.db import models
from django.utils import timezone
from house.models import House
from django.core.validators import MinValueValidator


class Expenses(models.Model):
    class Category(models.TextChoices):
        RENT = 'Rent'
        MORTGAGE = 'Mortgage'
        BILLS = 'Bills'
        TRANSPORTATION = 'Transportation'
        CLOTHING = 'Clothing'
        HEALTHCARE = 'Healthcare'
        FOOD = 'Food'
        INSURANCE = 'Insurance'
        KIDS = 'Kids'
        CULTURE = 'Culture'
        VACATIONS = 'Vacations'
        OTHER = 'Other'

    description = models.TextField(max_length=250, default='')
    category = models.CharField(max_length=32, choices=Category.choices, default=Category.OTHER)
    house_name = models.ForeignKey(House, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Category:{self.category},Amount:{self.amount}'

    @staticmethod
    def create_expense(house_name, amount, date, category):
        expense = Expenses(house_name=house_name, amount=amount, date=date, category=category)
        expense.save()
        return expense
