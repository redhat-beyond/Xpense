import pytest
from expenses.models import Expenses


@pytest.mark.django_db()
class TestExpensesModel:
    def test_save_expense(self, generate_expense):
        generate_expense.save()
        assert generate_expense in Expenses.objects.all()

    def test_delete_expense(self, generate_expense):
        generate_expense.save()
        generate_expense.house_name.delete()
        assert generate_expense not in Expenses.objects.all()
