import pytest

from factories.expense import ExpenseFactory
from factories.house import HouseFactory
from factories.user import UserFactory


@pytest.fixture
def user_factory():
    return UserFactory()


@pytest.fixture
def house_factory(user_factory):
    return HouseFactory(user=user_factory)


@pytest.fixture
def expense_factory(house_factory):
    return ExpenseFactory(house=house_factory, month=1)


@pytest.mark.django_db()
class TestFactories:
    def test_user_factory(self):
        UserFactory()

    def test_house_factory(self, user_factory):
        HouseFactory(user=user_factory)

    def test_expense_factory(self, house_factory):
        ExpenseFactory(house=house_factory, month=1)
