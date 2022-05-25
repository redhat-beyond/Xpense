import pytest
from house.constants import (
    MINE_ADD_EXPENSE_ROUTE,
    MINE_EXPENSES_TABLE_ROUTE,
    MINE_HOUSE_TABLE_ROUTE,
    MINE_PAGE_ROUTE,
    MINE_SIDEBAR_ROUTE,
)
from factories.house import HouseFactory
from expenses.models import Expenses
from django.template.loader import get_template
from tests.const import EXPENSE_FORM_DATA, EXPENSE_BAD_FORM_DATA_DESCRIPTION, EXPENSE_BAD_FORM_DATA_AMOUNT
from house.forms import ExpenseForm


@pytest.fixture
def client_login(client, new_user):
    client.force_login(new_user)


@pytest.fixture
def house_factory(client, new_user, client_login):
    house = HouseFactory(user=new_user).save()
    return house


@pytest.fixture
def generate_expense_form():
    form = ExpenseForm(EXPENSE_FORM_DATA)
    return form


@pytest.fixture
def generate_bad_description_expense_form():
    form = ExpenseForm(EXPENSE_BAD_FORM_DATA_DESCRIPTION)
    return form


@pytest.fixture
def generate_bad_amount_expense_form():
    form = ExpenseForm(EXPENSE_BAD_FORM_DATA_AMOUNT)
    return form


@pytest.mark.django_db
class TestExpenseForm:
    def test_expense_form(self, generate_expense_form):
        form = generate_expense_form
        assert form.is_valid()

    def test_bad_form_amount(self, generate_bad_amount_expense_form):
        form = generate_bad_amount_expense_form
        assert not form.is_valid()

    def test_bad_form_description(self, generate_bad_description_expense_form):
        form = generate_bad_description_expense_form
        assert not form.is_valid()


@pytest.mark.django_db
class TestMyHouseViewsAndTemplates:
    def test_get_house_view_function_and_templates(self, client, house_factory):
        response = client.get('/house/')
        assert response.status_code == 200
        get_template(MINE_PAGE_ROUTE)
        get_template(MINE_EXPENSES_TABLE_ROUTE)
        get_template(MINE_HOUSE_TABLE_ROUTE)
        get_template(MINE_SIDEBAR_ROUTE)


@pytest.mark.django_db
class TestAddExpenseToMyHouse:
    def test_add_expenses_to_my_house(self, client, house_factory):
        response = client.post('/house/add_expense/', EXPENSE_FORM_DATA)
        assert len(Expenses.objects.all()) == 1
        assert response.status_code == 302
        assert response.url == '/../house'

    def test_not_add_expenses_to_my_house_with_bad_description(self, client, house_factory):
        response = client.post('/house/add_expense/', EXPENSE_BAD_FORM_DATA_DESCRIPTION)
        assert len(Expenses.objects.all()) == 0
        assert response.status_code == 200

    def test_not_add_expenses_to_my_house_with_bad_amount(self, client, house_factory):
        response = client.post('/house/add_expense/', EXPENSE_BAD_FORM_DATA_AMOUNT)
        assert len(Expenses.objects.all()) == 0
        assert response.status_code == 200


@pytest.mark.django_db
class TestMyHouseAddExpenseViews:
    def test_get_add_expense_view_and_template(self, client, house_factory):
        response = client.get('/house/add_expense/')
        assert response.status_code == 200
        get_template(MINE_ADD_EXPENSE_ROUTE)
