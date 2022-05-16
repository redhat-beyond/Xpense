import pytest
from django.contrib.auth.models import User

from factories.user import UserFactory
from house.models import House, City, Country
from expenses.models import Expenses
from django.test.client import RequestFactory

from tests.const import HOUSE_NAME, HOUSE_PUBLIC, HOUSE_PARENT_PROFESSION_1, HOUSE_PARENT_PROFESSION_2, HOUSE_INCOME, \
    HOUSE_CHILDREN, HOUSE_DESCRIPTION, EXPENSE_AMOUNT, EXPENSE_DATE, EXPENSE_CATEGORY, USERNAME, FIRSTNAME, LASTNAME, \
    PASSWORD, EMAIL

BAD_FORM_DATA = {'house_id': '1234'}


@pytest.fixture
def generate_house(db):
    house = House.create_house(
        user=UserFactory(),
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


@pytest.fixture
def generate_expense(db, generate_house):
    return Expenses.create_expense(
        house_name=generate_house, amount=EXPENSE_AMOUNT, date=EXPENSE_DATE, category=EXPENSE_CATEGORY
    )


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def generate_get_request(request_factory):
    get_request = request_factory.get('login/')
    return get_request


@pytest.fixture
def new_user():
    user = User(username=USERNAME, first_name=FIRSTNAME, last_name=LASTNAME, password=PASSWORD, email=EMAIL)
    user.set_password(PASSWORD)
    user.save()
    return user
