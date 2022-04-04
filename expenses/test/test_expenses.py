import pytest
from django.utils import timezone
from expenses.models import Expenses
from house.models import House, Country, City

AMOUNT = '100'
DATE = timezone.now()
CATEGORY = 'Clothing'

HOUSE_NAME = "House 1"
HOUSE_PUBLIC = True
COUNTRY = "Colorado"
CITY = "South Park"
HOUSE_PARENT_PROFESSION_1 = "Teacher"
HOUSE_PARENT_PROFESSION_2 = "Student"
HOUSE_INCOME = 10_000
HOUSE_CHILDREN = 1


@pytest.fixture
def generate_country():
    return Country.create_country(name=COUNTRY)


@pytest.fixture
def generate_city(generate_country):
    return City.create_city(name=CITY, country=generate_country)


@pytest.fixture
def generate_house(generate_country, generate_city):
    house = House.create_house(
        name=HOUSE_NAME,
        public=HOUSE_PUBLIC,
        country=generate_country,
        city=generate_city,
        parent_profession_1=HOUSE_PARENT_PROFESSION_1,
        parent_profession_2=HOUSE_PARENT_PROFESSION_2,
        income=HOUSE_INCOME,
        children=HOUSE_CHILDREN,
    )
    return house


@pytest.fixture
def generate_expense(generate_house):
    return Expenses.create_expense(
        house_name=generate_house,
        amount=AMOUNT,
        date=DATE,
        category=CATEGORY
    )


@pytest.mark.django_db()
class TestExpensesModel:
    def test_new_expense(self, generate_expense):
        assert generate_expense.amount == AMOUNT
        assert generate_expense.date == DATE
        assert generate_expense.category == CATEGORY

    def test_save_expense(self, generate_expense):
        generate_expense.save()
        assert generate_expense in Expenses.objects.all()

    def test_delete_expense(self, generate_expense):
        generate_expense.save()
        generate_expense.house_name.delete()
        assert generate_expense not in Expenses.objects.all()
