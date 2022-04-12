import pytest
from django.utils import timezone
from house.models import House, City, Country
from expenses.models import Expenses

HOUSE_NAME = "House 1"
HOUSE_PUBLIC = True
HOUSE_PARENT_PROFESSION_1 = "Teacher"
HOUSE_PARENT_PROFESSION_2 = "Student"
HOUSE_INCOME = 10_000
HOUSE_CHILDREN = 1
HOUSE_DESCRIPTION = "description"


@pytest.fixture
def generate_house(db):
    house = House.create_house(
        name=HOUSE_NAME,
        public=HOUSE_PUBLIC,
        country=Country.objects.get(name="Israel"),
        city=City.objects.get(name="Tel Aviv"),
        parent_profession_1=HOUSE_PARENT_PROFESSION_1,
        parent_profession_2=HOUSE_PARENT_PROFESSION_2,
        income=HOUSE_INCOME,
        children=HOUSE_CHILDREN,
        description=HOUSE_DESCRIPTION,
    )
    return house


AMOUNT = 100
DATE = timezone.now()
CATEGORY = Expenses.Category.CLOTHING


@pytest.fixture
def generate_expense(db, generate_house):
    return Expenses.create_expense(house_name=generate_house, amount=AMOUNT, date=DATE, category=CATEGORY)
