import pytest
from house.constants import (
    MINE_ADD_EXPENSE_ROUTE,
    MINE_EXPENSES_TABLE_ROUTE,
    MINE_HOUSE_TABLE_ROUTE,
    MINE_PAGE_ROUTE,
    MINE_SIDEBAR_ROUTE,
    MINE_EDIT_EXPENSE_ROUTE,
    MINE_EDIT_HOUSE,
    MINE_CHARTS_ROUTE,
)
from factories.expense import ExpenseFactory
from factories.house import HouseFactory
from expenses.models import Expenses
from tests.const import (
    EXPENSE_FORM_DATA,
    EXPENSE_BAD_FORM_DATA_DESCRIPTION,
    EXPENSE_BAD_FORM_DATA_AMOUNT,
    EXPENSE_DESCRIPTION_BEFORE,
    EXPENSE_DESCRIPTION_AFTER,
    EXPENSE_AMOUNT,
    EXPENSE_DATE,
    EXPENSE_CATEGORY,
    HOUSE_NAME,
    HOUSE_PUBLIC,
    HOUSE_PARENT_PROFESSION_1,
    HOUSE_PARENT_PROFESSION_2,
    HOUSE_INCOME,
    HOUSE_CHILDREN_BEFORE,
    HOUSE_CHILDREN_AFTER,
    HOUSE_DESCRIPTION,
    COUNTRY,
    CITY,
    COUNTY_OR_CITY,
)
from house.forms import ExpenseForm
from house.models import House, City, Country


@pytest.fixture
def client_login(client, new_user):
    client.force_login(new_user)


@pytest.fixture
def house_factory(client, new_user):
    client.force_login(new_user)
    house = HouseFactory(user=new_user)
    house.save()
    return house


@pytest.fixture
def expense_factory(client, new_user, client_login, house_factory):
    expense = ExpenseFactory(house=house_factory, month=1).save()
    return expense


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

        template_names = set(template.origin.template_name for template in response.templates)
        assert MINE_PAGE_ROUTE in template_names
        assert MINE_EXPENSES_TABLE_ROUTE in template_names
        assert MINE_HOUSE_TABLE_ROUTE in template_names
        assert MINE_SIDEBAR_ROUTE in template_names
        assert MINE_CHARTS_ROUTE in template_names

    def test_get_add_expense_view_and_template(self, client, house_factory):
        response = client.get('/house/add_expense/')
        assert response.status_code == 200

        template_names = set(template.origin.template_name for template in response.templates)
        assert MINE_ADD_EXPENSE_ROUTE in template_names

    def test_get_edit_expense_view_function_and_templates(self, client, house_factory, expense_factory):
        response = client.get('/house/edit_expense/1/')
        assert response.status_code == 200

        template_names = set(template.origin.template_name for template in response.templates)
        assert MINE_EDIT_EXPENSE_ROUTE in template_names

    def test_get_delete_expense_view(self, client, house_factory, expense_factory):
        response = client.get('/house/delete_expense/1/')
        assert response.status_code == 302

    def test_get_edit_house_view_function_and_templates(self, client, house_factory):
        response = client.get('/house/edit_house/')
        assert response.status_code == 200

        template_names = set(template.origin.template_name for template in response.templates)
        assert MINE_EDIT_HOUSE in template_names


@pytest.mark.django_db
class TestActionsOnExpensesOfMyHouse:
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

    def test_edit_expenses_of_my_house(self, client, house_factory):
        expense = Expenses.create_expense(
            house_name=house_factory,
            amount=EXPENSE_AMOUNT,
            date=EXPENSE_DATE,
            category=EXPENSE_CATEGORY,
            description=EXPENSE_DESCRIPTION_BEFORE,
        )
        expense.save()
        response = client.post(
            '/house/edit_expense/1/',
            {
                'amount': EXPENSE_AMOUNT,
                'date': EXPENSE_DATE,
                'category': EXPENSE_CATEGORY,
                'description': EXPENSE_DESCRIPTION_AFTER,
            },
        )
        edited_expense: Expenses = Expenses.objects.all()[0]
        assert edited_expense.description == EXPENSE_DESCRIPTION_AFTER
        assert len(Expenses.objects.all()) == 1
        assert response.status_code == 302
        assert response.url == '/../house'

    def test_delete_expenses_of_my_house(self, client, house_factory, expense_factory):
        response = client.post('/house/delete_expense/1/', EXPENSE_FORM_DATA)
        assert len(Expenses.objects.all()) == 0
        assert response.status_code == 302
        assert response.url == '/../house'

    def test_edit_existing_house(self, client, house_factory, new_user):
        client.force_login(new_user)
        country = Country.create_country(COUNTRY)
        house = House.create_house(
            user=new_user,
            name=HOUSE_NAME,
            public=HOUSE_PUBLIC,
            country=country,
            city=City.create_city(CITY, country),
            parent_profession_1=HOUSE_PARENT_PROFESSION_1,
            parent_profession_2=HOUSE_PARENT_PROFESSION_2,
            income=HOUSE_INCOME,
            children=HOUSE_CHILDREN_BEFORE,
            description=HOUSE_DESCRIPTION,
        )
        house.save()
        house_form = {
            'public': house.public,
            'country': COUNTY_OR_CITY,
            'city': COUNTY_OR_CITY,
            'parent_profession_1': house.parent_profession_1,
            'parent_profession_2': house.parent_profession_2,
            'children': house.children,
            'income': house.income,
            'name': house.name,
        }
        response = client.post('/house_create/', data=house_form)
        house_form = {
            'public': house.public,
            'country': COUNTY_OR_CITY,
            'city': COUNTY_OR_CITY,
            'parent_profession_1': house.parent_profession_1,
            'parent_profession_2': house.parent_profession_2,
            'children': HOUSE_CHILDREN_AFTER,
            'income': house.income,
            'name': house.name,
        }
        response = client.post('/house/edit_house/', data=house_form)
        edited_house: House = House.objects.all()[0]
        assert edited_house.children == HOUSE_CHILDREN_AFTER
        assert len(House.objects.all()) == 1
        assert response.status_code == 302
        assert response.url == '/../house'
