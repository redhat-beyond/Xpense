from django.template import TemplateDoesNotExist
from factories.house import HouseFactory
from factories.user import UserFactory
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

    def test_global_doesnt_show_private_houses(self, db, client):
        HouseFactory(user=UserFactory(), public=False)
        HouseFactory(user=UserFactory(), public=True)
        render = client.get('/global/')
        houses_in_global = render.context["all_houses"]
        assert houses_in_global.filter(public=True).count() == 1
        assert houses_in_global.filter(public=False).count() == 0, "Private houses are shown"
