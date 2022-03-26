import pytest
from django.utils import timezone
from .models import Expenses

AMOUNT = '100'
DATE = timezone.now()
CATEGORY = 'CLOTHING'


@pytest.fixture
def expense_test0():
    return Expenses(amount=AMOUNT,
                    date=DATE,
                    Category=CATEGORY
                    )


@pytest.mark.django_db
class TestExpenseדModel:
    def test_create_expense(self, expense_test0):
        assert expense_test0.amount == AMOUNT
        assert expense_test0.date == DATE
        assert expense_test0.Category == CATEGORY


def test_save_expense(self, expense_test0):
    expense_test0.save()
    assert expense_test0 in Expenses.objects.all()


def test_delete_expense(self, expense_test0):
    expense_test0.save()
    expense_test0.delete()
    assert expense_test0 not in Expenses.objects.all()
