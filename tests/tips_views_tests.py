import pytest
from django.utils import timezone
from django.shortcuts import get_object_or_404
from tips.models import Tip
from django.template import TemplateDoesNotExist
from tips.forms import TipForm
from django.template.loader import get_template
from tips.constants import TIPS_PAGE_ROUTE, ADD_TIP_PAGE_ROUTE, EDIT_TIP_PAGE_ROUTE

AUTHOR = 'RICK'
OTHER_AUTHOR = 'RICKEN'
CATEGORY = 'Clothing'
OTHER_CATEGORY = 'Food'
DATE = timezone.now()
TEXT = 'I BOUGHT A TESLA IN 50$ DISCOUNT IN LEVINSKI MARKET'
OTHER_TEXT = 'Let them eat cake'

FORM_DATA = {'author': OTHER_AUTHOR, 'text': OTHER_TEXT, 'category': OTHER_CATEGORY}
BAD_FORM_DATA = {'author': OTHER_AUTHOR, 'text': '', 'category': CATEGORY}


@pytest.fixture
def generate_tip():
    return Tip.create_tip(
        category=CATEGORY,
        author=AUTHOR,
        date=DATE,
        text=TEXT,
    )


@pytest.fixture
def generate_form():
    form = TipForm(FORM_DATA)
    return form


@pytest.fixture
def generate_bad_form():
    form = TipForm(BAD_FORM_DATA)
    return form


@pytest.mark.django_db
class TestTipForms:
    def test_form(self, db, generate_form):
        form = generate_form
        assert form.is_valid()

    def test_add_tip(self, generate_form):
        form = generate_form
        tip = form.save()
        assert tip in Tip.objects.all()

    def test_edit_tip(self, generate_form, generate_tip):
        generate_tip.save()
        tip = get_object_or_404(Tip, pk=generate_tip.id)
        assert tip.author == AUTHOR
        assert tip.category == CATEGORY
        assert tip.text == TEXT
        form = generate_form
        tip = form.save(commit=False)
        tip.save()
        assert tip.author == OTHER_AUTHOR
        assert tip.category == OTHER_CATEGORY
        assert tip.text == OTHER_TEXT

    def test_bad_form(self, generate_bad_form):
        form = generate_bad_form
        assert not form.is_valid()


@pytest.mark.django_db
class TestTipViews:
    def test_tips_board_function_200(self, client):
        response = client.get('/tips/')
        assert response.status_code == 200
        assert 'Tips' in str(response.content)

    def test_tips_views_templates(self):
        try:
            get_template(TIPS_PAGE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {TIPS_PAGE_ROUTE} does not exist"
        try:
            get_template(ADD_TIP_PAGE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {ADD_TIP_PAGE_ROUTE} does not exist"
        try:
            get_template(EDIT_TIP_PAGE_ROUTE)
        except TemplateDoesNotExist:
            assert False, f"Template {EDIT_TIP_PAGE_ROUTE} does not exist"

    def test_delete_tip_function(self, client, generate_tip):
        generate_tip.save()
        assert generate_tip in Tip.objects.all()
        client.get('/tips/delete_tip/' + str(generate_tip.id) + '/')
        assert generate_tip not in Tip.objects.all()
