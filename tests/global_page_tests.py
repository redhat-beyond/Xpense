from django.template import TemplateDoesNotExist
from house.constants import GLOBAL_PAGE_ROUTE
from django.template.loader import get_template


class TestGlobalPage:
    def test_global_template(self):
        try:
            get_template(GLOBAL_PAGE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {GLOBAL_PAGE_ROUTE} does not exist"

    def test_global_function_200(self, db, client):
        render = client.get('/global/')
        assert render.status_code == 200, "Status code is not 200"
