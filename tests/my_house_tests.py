import pytest
from house.constants import MINE_ADD_EXPENSE_ROUTE, MINE_EXPENSES_TITLE_ROUTE, \
    MINE_HOUSE_TABLE_ROUTE, MINE_HOUSE_TABLE_TITLE_ROUTE, MINE_MINE_PAGE_ROUTE, MINE_SIDEBAR_ROUTE
from factories.house import HouseFactory
from house.views import add_expense, house_view
from house.models import House
from house.forms import ExpenseForm
from expenses.models import Expenses
from django.test.client import RequestFactory
from django.utils import timezone
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

HOUSE_NAME = "House 1"
HOUSE_PUBLIC = True
COUNTRY = "Colorado"
CITY = "South Park"
HOUSE_PARENT_PROFESSION_1 = "Teacher"
HOUSE_PARENT_PROFESSION_2 = "Student"
HOUSE_INCOME = 10_000
HOUSE_CHILDREN = 1

AMOUNT = 100
DATE = timezone.now()
CATEGORY = 'Clothing'
DESCRIPTION = 'DESCRIPTION'

BAD_AMOUNT = -100
BAD_DESCRIPTION = ''

EXPENSE_FORM_DATA = {'date': DATE, 'amount': AMOUNT, 'category': CATEGORY, 'description': DESCRIPTION}
EXPENSE_BAD_FORM_DATA_AMOUNT = {'date': DATE, 'amount': BAD_AMOUNT, 'category': CATEGORY, 'description': DESCRIPTION}
EXPENSE_BAD_FORM_DATA_DESCRIPTION = {'date': DATE, 'amount': AMOUNT, 'category': CATEGORY,
                                     'description': BAD_DESCRIPTION}


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def generate_get_request(request_factory):
    get_request = request_factory.get('<str:house_id>/add_expense/')
    return get_request


@pytest.fixture
def generate_expense_form(request_factory):
    post_request = request_factory.post('<str:house_id>/add_expense/', EXPENSE_FORM_DATA)
    form = ExpenseForm(post_request.POST)
    return form


@pytest.fixture
def generate_bad_expense_form_description(request_factory):
    post_request = request_factory.post('<str:house_id>/add_expense/', EXPENSE_BAD_FORM_DATA_DESCRIPTION)
    form = ExpenseForm(post_request.POST)
    return form


@pytest.fixture
def generate_bad_expense_form_amount(request_factory):
    post_request = request_factory.post('<str:house_id>/add_expense/', EXPENSE_BAD_FORM_DATA_AMOUNT)
    form = ExpenseForm(post_request.POST)
    return form


@pytest.mark.django_db
class TestMyHouseViews:
    def test_house_view_function_200(self, generate_get_request):
        HouseFactory().save()
        house = House.objects.all()[0]
        try:
            render = house_view(generate_get_request, house.house_id)
            assert render.status_code == 200, "Status code is not 200"
        except Exception:
            assert False, "Error in house_view function"

    def test_mine_page_expenses_table_views_templates(self):
        try:
            get_template(MINE_EXPENSES_TITLE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {MINE_EXPENSES_TITLE_ROUTE} does not exist"

    def test_mine_page_house_table_views_templates(self):
        try:
            get_template(MINE_HOUSE_TABLE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {MINE_HOUSE_TABLE_ROUTE} does not exist"

    def test_mine_page_house_table_title_views_templates(self):
        try:
            get_template(MINE_HOUSE_TABLE_TITLE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {MINE_HOUSE_TABLE_TITLE_ROUTE} does not exist"

    def test_mine_page_mine_page_views_templates(self):
        try:
            get_template(MINE_MINE_PAGE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {MINE_MINE_PAGE_ROUTE} does not exist"

    def test_mine_sidebar_views_templates(self):
        try:
            get_template(MINE_SIDEBAR_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {MINE_SIDEBAR_ROUTE} does not exist"


@pytest.mark.django_db
class TestExpenseForm:
    def test_expense_form(self, generate_expense_form):
        form = generate_expense_form
        assert form.is_valid()

    def test_bad_form_amount(self, generate_bad_expense_form_amount):
        form = generate_bad_expense_form_amount
        assert not form.is_valid()

    def test_bad_form_description(self, generate_bad_expense_form_description):
        form = generate_bad_expense_form_description
        assert not form.is_valid()

    def test_add_expenses_to_my_house(self, request_factory):
        house = HouseFactory()
        house.save()
        post_request = request_factory.post(f'{house.house_id}/add_expense/', EXPENSE_FORM_DATA)
        add_expense(post_request, house.house_id)
        assert len(Expenses.objects.all()) == 1


@pytest.mark.django_db
class TestMyHouseAddExpenseViews:
    def test_get_add_expense_view(self, client):
        HouseFactory().save()
        house = House.objects.all()[0]
        response = client.get(f'/{house.house_id}/add_expense/')
        assert response.status_code == 200

    def test_mine_page_add_expense_views_templates(self):
        try:
            get_template(MINE_ADD_EXPENSE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {MINE_ADD_EXPENSE_ROUTE} does not exist"
