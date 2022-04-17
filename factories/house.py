import random

import factory
from factory.django import DjangoModelFactory

from house.models import House, Country, City, Job


class HouseFactory(DjangoModelFactory):
    class Meta:
        model = House

    name = factory.Faker('name')
    public = factory.Faker('boolean')
    country = factory.Iterator(Country.objects.all())
    city = factory.LazyAttribute(lambda x: random.choice(City.objects.filter(country=x.country)))
    parent_profession_1 = factory.LazyAttribute(lambda x: random.choice([tup[1] for tup in Job.choices]))
    parent_profession_2 = factory.LazyAttribute(lambda x: random.choice([tup[1] for tup in Job.choices]))
    income = factory.Faker('random_number', digits=5)
    children = factory.Faker('random_number', digits=1)
