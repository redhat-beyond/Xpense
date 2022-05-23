import pytest
from django.contrib.auth.models import User
from factories.user import UserFactory
from django.core.management import call_command
from house.models import House, City, Country
from expenses.models import Expenses

from tests.const import (
    HOUSE_NAME,
    HOUSE_PUBLIC,
    HOUSE_PARENT_PROFESSION_2,
    HOUSE_PARENT_PROFESSION_1,
    HOUSE_INCOME,
    HOUSE_CHILDREN,
    HOUSE_DESCRIPTION,
    EXPENSE_AMOUNT,
    EXPENSE_DATE,
    EXPENSE_CATEGORY,
    USERNAME,
    PASSWORD,
    FIRSTNAME,
    LASTNAME,
    EMAIL,
)


@pytest.fixture
def generate_house(db):
    house = House.create_house(
        user=UserFactory(),
        name=HOUSE_NAME,
        public=HOUSE_PUBLIC,
        country=Country.objects.get(name='Israel'),
        city=City.objects.get(name='Tel Aviv'),
        parent_profession_1=HOUSE_PARENT_PROFESSION_1,
        parent_profession_2=HOUSE_PARENT_PROFESSION_2,
        income=HOUSE_INCOME,
        children=HOUSE_CHILDREN,
        description=HOUSE_DESCRIPTION,
    )
    return house


@pytest.fixture
def generate_expense(db, generate_house):
    return Expenses.create_expense(
        house_name=generate_house, amount=EXPENSE_AMOUNT, date=EXPENSE_DATE, category=EXPENSE_CATEGORY
    )


@pytest.fixture
def new_user():
    user = User(username=USERNAME, first_name=FIRSTNAME, last_name=LASTNAME, password=PASSWORD, email=EMAIL)
    user.set_password(PASSWORD)
    user.save()
    return user


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    fixtures = ['countries_cities']

    with django_db_blocker.unblock():
        call_command('loaddata', *fixtures)
