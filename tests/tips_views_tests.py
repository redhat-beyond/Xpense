import pytest
from django.utils import timezone
from django.shortcuts import get_object_or_404
from tips.models import Tip
from tips.forms import TipForm
from django.template.loader import get_template
from django.contrib.auth.models import User
from tips.constants import (
    TIPS_PAGE_ROUTE,
    ADD_TIP_PAGE_ROUTE,
    EDIT_TIP_PAGE_ROUTE,
    READ_MORE_PAGE_ROUTE,
    CATEGORIES_PAGE_ROUTE,
)

AUTHOR = 'RICK'
OTHER_AUTHOR = 'RICKEN'
CATEGORY = 'Clothing'
OTHER_CATEGORY = 'Food'
DATE = timezone.now()
TEXT = 'I BOUGHT A TESLA IN 50$ DISCOUNT IN LEVINSKI MARKET'
OTHER_TEXT = 'Let them eat cake'
OTHER_CATEGORY = 'Kids'
OTHER_DATE = '2001-01-01'

FORM_DATA = {'author': OTHER_AUTHOR, 'text': TEXT, 'category': CATEGORY}
BAD_FORM_DATA = {'author': OTHER_AUTHOR, 'text': '', 'category': CATEGORY}


@pytest.fixture
def generate_tip(**kwargs):
    def _tip_factory(**kwargs) -> Tip:
        tip_category = kwargs.pop('category', 'Other')
        tip_author = kwargs.pop('author', 'Other')
        tip_date = kwargs.pop('date', timezone.now())
        tip_text = kwargs.pop('text', 'Other')

        return Tip.objects.create(author=tip_author, date=tip_date, text=tip_text, category=tip_category, **kwargs)

    return _tip_factory


@pytest.fixture
def generate_form():
    form = TipForm(FORM_DATA)
    return form


@pytest.fixture
def generate_bad_form():
    form = TipForm(BAD_FORM_DATA)
    return form


@pytest.mark.django_db()
class TestTipForms:
    def test_form(self, db, generate_form):
        form = generate_form
        assert form.is_valid()

    def test_add_tip(self, generate_form):
        form = generate_form
        tip = form.save()
        assert tip in Tip.objects.all()

    def test_edit_tip(self, generate_tip, generate_form):
        test_tip = generate_tip(author=AUTHOR, date=DATE, text=TEXT, category=CATEGORY)
        test_tip.save()
        tip = get_object_or_404(Tip, pk=test_tip.id)
        assert tip.author == AUTHOR
        assert tip.category == CATEGORY
        assert tip.text == TEXT
        tip = generate_form.save(commit=False)
        tip.save()
        assert tip.author == OTHER_AUTHOR
        assert tip.category == CATEGORY
        assert tip.text == TEXT

    def test_bad_form(self, generate_bad_form):
        form = generate_bad_form
        assert not form.is_valid()


@pytest.mark.django_db
class TestTipViews:
    def test_tips_views_tips_template(self):
        get_template(TIPS_PAGE_ROUTE)

    def test_tips_views_add_tip_template(self):
        get_template(ADD_TIP_PAGE_ROUTE)

    def test_tips_views_edit_tip_template(self):
        get_template(EDIT_TIP_PAGE_ROUTE)

    def test_tips_views_read_more_template(self):
        get_template(READ_MORE_PAGE_ROUTE)

    def test_tips_views_categories_template(self):
        get_template(CATEGORIES_PAGE_ROUTE)

    def test_delete_tip_function(self, client, generate_tip):
        test_tip = generate_tip(author=AUTHOR, date=DATE, text=TEXT, category=CATEGORY)
        test_tip.save()
        assert test_tip in Tip.objects.all()
        if User.get_session_auth_hash == test_tip.user_token:
            client.get('/tips/delete_tip/' + str(test_tip.id) + '/')
            assert test_tip not in Tip.objects.all()
        else:
            test_tip in Tip.objects.all()

    # Creates different tips and return the tip to filter by
    def test_create_tips(self, generate_tip):
        test_tip = generate_tip(author=AUTHOR, date=DATE, text=TEXT, category=CATEGORY)
        test_tip.save()
        tip_to_filter_by = generate_tip(author=OTHER_AUTHOR, date=OTHER_DATE, text=OTHER_TEXT, category=OTHER_CATEGORY)
        tip_to_filter_by.save()

        return tip_to_filter_by

    def test_filtered_tips_by_category(self, client, generate_tip):
        tip_to_filter_by = self.test_create_tips(generate_tip)
        tips = Tip.objects.all()
        assert len(tips) == 2
        response = client.get('/tips/category/' + tip_to_filter_by.category + '/')
        tips = response.context['category_filtered_tips']
        assert len(tips) == 1

    def test_filtered_tips_by_date(self, client, generate_tip):
        tip_to_filter_by = self.test_create_tips(generate_tip)
        tips = Tip.objects.all()
        assert len(tips) == 2
        response = client.get('/tips/filtered_by_date/' + tip_to_filter_by.date + '/')
        tips = response.context['filtered_tips_by_date']
        assert len(tips) == 1
