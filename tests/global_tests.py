import pytest
from house.models import House
from expenses.models import Expenses
from django.template import TemplateDoesNotExist
from django.test.client import RequestFactory
from house.constants import GLOBAL_PAGE
from house.forms import HouseForm
from house.views import global_page, filter_houses_by_form, average_expenses_of_houses_by_categories
from django.template.loader import get_template

# Form Data That corresponds to the House data generated in conftest.py
FORM_DATA_CORRECT = {
    'country': ['2'],
    'city': ['2'],
    'parent_profession_1': ['Student'],
    'parent_profession_2': ['Teacher'],
    'income': ['10000'],
    'children': ['1'],
}


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def generate_get_request(request_factory):
    get_request = request_factory.get('global/')
    return get_request


@pytest.fixture
def generate_form(request_factory):
    post_request = request_factory.post(
        'global/',
        FORM_DATA_CORRECT,
    )
    form = HouseForm(post_request.POST)
    return form


# I take the correct form and create a wrong from for each field and return a list of the wrong forms
@pytest.fixture
def generate_wrong_form_list(request_factory):
    wrong_forms_list = []
    for key, value in FORM_DATA_CORRECT.items():
        try:
            new_value = [str(int(value[0])+1)]  # add 1 to the value of form
        except ValueError:
            new_value = ['Other']
        WRONG_FORM = {**FORM_DATA_CORRECT, key: new_value}
        post_request = request_factory.post(
            'global/',
            WRONG_FORM,
        )
        wrong_forms_list.append(HouseForm(post_request.POST))
    return wrong_forms_list


class TestGlobalPage:
    def test_global_template(self):
        try:
            get_template(GLOBAL_PAGE)
        except TemplateDoesNotExist:
            assert False, f"Template {GLOBAL_PAGE} does not exist"

    def test_global_function_200(self, db, generate_get_request):
        try:
            render = global_page(generate_get_request)
            assert render.status_code == 200, "Status code is not 200"
        except Exception:
            assert False, "Error in global_page function"

    def test_house_filtering_not_filter_house(self, db, generate_form, generate_house):
        houses = filter_houses_by_form(generate_form, House.objects.all())
        assert generate_house in houses, "House was filtered"
    
    def test_house_filtering_do_filter_house(self, db, generate_wrong_form_list, generate_house):
        for form in generate_wrong_form_list:
            houses = House.objects.all()
            houses = filter_houses_by_form(form, houses)
            assert generate_house not in houses, "House was not filtered"
            
    def test_average_expenses_of_houses_by_categories(self, db, generate_house, generate_expense):
        Expenses.create_expense(house_name=generate_house, amount=0,
                                date=generate_expense.date, category=generate_expense.category)
        avg = average_expenses_of_houses_by_categories(House.objects.all())
        assert avg[0]['category'] == generate_expense.category, "Category is not correct"
        assert avg[0]['average'] == generate_expense.amount / 2, "Average is not correct"
