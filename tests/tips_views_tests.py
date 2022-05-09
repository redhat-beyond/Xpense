import pytest
from django.utils import timezone
from django.shortcuts import get_object_or_404
from tips.models import Tip
from django.template import TemplateDoesNotExist
from django.test.client import RequestFactory
from tips.forms import TipForm
from tips.views import board, delete_tip
from django.template.loader import get_template
from tips.constants import TIPS_PAGE_ROUTE, ADD_TIP_PAGE_ROUTE, EDIT_TIP_PAGE_ROUTE

AUTHOR = 'RICK'
OTHER_AUTHOR = 'RICKEN'
CATEGORY = 'Clothing'
DATE = timezone.now()
TEXT = 'I BOUGHT A TESLA IN 50$ DISCOUNT IN LEVINSKI MARKET'

FORM_DATA = {'author': OTHER_AUTHOR, 'text': TEXT, 'category': CATEGORY}
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
def request_factory():
    return RequestFactory()


@pytest.fixture
def generate_form(request_factory):
    post_request = request_factory.post(
        'tips/add_tip',
        FORM_DATA,
    )
    form = TipForm(post_request.POST)
    return form


@pytest.fixture
def generate_bad_form(request_factory):
    post_request = request_factory.post('tips/add_tip', BAD_FORM_DATA)
    form = TipForm(post_request.POST)
    return form


@pytest.fixture
def generate_get_request(request_factory):
    get_request = request_factory.get('tips/')
    return get_request


@pytest.mark.django_db
class TestTipForms:
    def test_form(self, db, generate_form, generate_tip):
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
        form = generate_form
        tip = form.save(commit=False)
        tip.save()
        assert tip.author == OTHER_AUTHOR

    def test_bad_form(self, generate_bad_form):
        form = generate_bad_form
        assert not form.is_valid()


@pytest.mark.django_db
class TestTipViews:
    def test_tips_board_function_200(self, generate_get_request, generate_tip):
        try:
            render = board(generate_get_request)
            assert render.status_code == 200, "status code is not 200"
        except Exception:
            assert False, "Error in board function"

    def test_tips_views_templates(self):
        try:
            get_template('tips/board.html')
        except TemplateDoesNotExist:
            assert False, f"Template {TIPS_PAGE_ROUTE} does not exist"
        try:
            get_template('tips/add_tip.html')
        except TemplateDoesNotExist:
            assert False, f"Template {ADD_TIP_PAGE_ROUTE} does not exist"
        try:
            get_template('tips/edit_tip.html')
        except TemplateDoesNotExist:
            assert False, f"Template {EDIT_TIP_PAGE_ROUTE} does not exist"

    def test_delete_tip_page(self, generate_get_request, generate_tip):
        generate_tip.save()
        delete_tip(generate_get_request, generate_tip.id)
        assert generate_tip not in Tip.objects.all()
