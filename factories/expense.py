from datetime import timezone, datetime, timedelta
import factory
from factory.django import DjangoModelFactory
import random

from house.models import House
from expenses.models import Expenses


class ExpenseFactory(DjangoModelFactory):
    class Meta:
        model = Expenses

    class Params:
        house: House = None
        month: datetime.month = 0

    @staticmethod
    def last_day_of_month(any_day):
        next_month = any_day.replace(day=28) + timedelta(days=4)
        return next_month - timedelta(days=next_month.day)

    @staticmethod
    def random_date(month):
        start_date = datetime.today().replace(day=1, month=month, tzinfo=timezone.utc)
        end_date = ExpenseFactory.last_day_of_month(start_date)

        return start_date + timedelta(
            seconds=random.randint(0, int((end_date - start_date).total_seconds())),
        )

    house_name = factory.LazyAttribute(lambda x: x.house if x.house else House.objects.order_by('?').first())
    category = factory.LazyAttribute(lambda x: random.choice([tup[1] for tup in Expenses.Category.choices]))
    amount = factory.LazyAttribute(lambda x: random.randint(5000, 25000))
    date = factory.LazyAttribute(lambda x: ExpenseFactory.random_date(x.month))
    description = ""
