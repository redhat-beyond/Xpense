import pytest
from django.utils import timezone
from tips.models import Tip

AUTHOR = 'RICK'
DATE = timezone.now()
CATEGORY = 'Clothing'
TEXT = 'I BOUGHT A TESLA IN 50$ DISCOUNT IN LEVINSKI MARKET'


@pytest.fixture
def generate_tip():
    return Tip.create_tip(
        category=CATEGORY,
        author=AUTHOR,
        date=DATE,
        text=TEXT,
    )


@pytest.mark.django_db
class TestTipModel:
    def test_create_tip(self, generate_tip):
        assert generate_tip.category == CATEGORY
        assert generate_tip.author == AUTHOR
        assert generate_tip.date == DATE
        assert generate_tip.text == TEXT

    def test_save_tip(self, generate_tip):
        generate_tip.save()
        assert generate_tip in Tip.objects.all()

    def test_delete_tip(self, generate_tip):
        generate_tip.save()
        generate_tip.delete()
        assert generate_tip not in Tip.objects.all()
