import random
import factory

from house.models import House
from expenses.models import Expenses


class ExpenseFactory(factory.Factory):
    class Meta:
        model = Expenses

    description = ""
    house_name = factory.Iterator(House.objects.all())
    category = factory.LazyAttribute(lambda x: random.choice([tup[1] for tup in Expenses.Category.choices]))
    amount = factory.LazyAttribute(lambda x: random.randint(5000, 25000))
    date = factory.Faker('date_object')
