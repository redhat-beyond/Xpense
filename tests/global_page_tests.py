import pytest
from django.template import TemplateDoesNotExist
from django.test.client import RequestFactory
from house.constants import GLOBAL_PAGE_ROUTE
from django.template.loader import get_template
from house.views import global_page


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def generate_get_request(request_factory):
    get_request = request_factory.get('global/')
    return get_request


class TestGlobalPage:
    def test_global_template(self):
        try:
            get_template(GLOBAL_PAGE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {GLOBAL_PAGE_ROUTE} does not exist"

    def test_global_function_200(self, db, generate_get_request):
        try:
            render = global_page(generate_get_request)
            assert render.status_code == 200, "Status code is not 200"
        except Exception:
            assert False, "Error in global_page function"
