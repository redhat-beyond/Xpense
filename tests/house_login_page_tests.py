import pytest
from house.constants import LOGIN_PAGE_ROUTE
from house.views import house_login
from house.models import House
from factories.house import HouseFactory
from django.test.client import RequestFactory
from house.forms import HouseIDForm
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

BAD_FORM_DATA = {'house_id': '1234'}


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


@pytest.mark.django_db
class TestLoginViews:
    def test_login_template(self):
        try:
            get_template(LOGIN_PAGE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {LOGIN_PAGE_ROUTE} does not exist"

    def test_login_page_function_200(self, generate_get_request):
        try:
            render = house_login(generate_get_request)
            assert render.status_code == 200, "status code is not 200"
        except Exception:
            assert False, "Error in house_login function"


@pytest.mark.django_db
class TestLoginForms:
    def test_form(self, generate_form):
        form = generate_form
        assert form.is_valid()

    def test_bad_form(self, generate_bad_form):
        form = generate_bad_form
        assert not form.is_valid()
