import pytest
from django.utils import timezone
from house.models import House, City, Country
from expenses.models import Expenses
from factories.house import HouseFactory
from django.test.client import RequestFactory
from house.forms import HouseIDForm

HOUSE_NAME = "House 1"
HOUSE_PUBLIC = True
HOUSE_PARENT_PROFESSION_1 = "Teacher"
HOUSE_PARENT_PROFESSION_2 = "Student"
HOUSE_INCOME = 10_000
HOUSE_CHILDREN = 1
HOUSE_DESCRIPTION = "description"

EXPENSE_AMOUNT = 100
EXPENSE_DATE = timezone.now()
EXPENSE_CATEGORY = Expenses.Category.CLOTHING

BAD_FORM_DATA = {'house_id': '1234'}


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
def generate_form(request_factory):
    HouseFactory().save()
    house = House.objects.all()[0]
    post_request = request_factory.post('login/', {'house_id': f'{house.house_id}'})
    form = HouseIDForm(post_request.POST)
    return form


@pytest.fixture
def generate_bad_form(request_factory):
    post_request = request_factory.post('login/', BAD_FORM_DATA)
    form = HouseIDForm(post_request.POST)
    return form
