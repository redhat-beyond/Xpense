import pytest
from expenses.models import Expenses
from factories.house import HouseFactory
from factories.user import UserFactory
from house.models import House
# from tests.const import DATE
from django.utils import timezone



@pytest.mark.django_db()
class TestExpensesModel:
    def test_save_expense(self, generate_expense):
        generate_expense.save()
        assert generate_expense in Expenses.objects.all()

    def test_delete_expense(self, generate_expense):
        generate_expense.save()
        generate_expense.house_name.delete()
        assert generate_expense not in Expenses.objects.all()


def _helper_create_houses():
    house_1 = HouseFactory(user=UserFactory())
    house_2 = HouseFactory(user=UserFactory())
    Expenses(house_name=house_1, amount=100, date=timezone.now(), category=Expenses.Category.FOOD).save()
    Expenses(house_name=house_1, amount=200, date=timezone.now(), category=Expenses.Category.FOOD).save()
    Expenses(house_name=house_2, amount=300, date=timezone.now(), category=Expenses.Category.FOOD).save()
    Expenses(house_name=house_2, amount=300, date=timezone.now(), category=Expenses.Category.KIDS).save()
    Expenses(house_name=house_2, amount=400, date=timezone.now(), category=Expenses.Category.KIDS).save()


@pytest.mark.django_db()
class TestExpensesFunctions:
    def test_average_expenses_of_houses_by_categories(self):
        _helper_create_houses()
        houses = House.objects.all()
        avg_expenses_by_categories = Expenses.average_expenses_of_houses_by_categories(houses=houses)
        assert avg_expenses_by_categories[0]['average'] == 200
        assert avg_expenses_by_categories[1]['average'] == 350
