import random
from factories.expense import ExpenseFactory
from factories.house import HouseFactory
from factories.user import UserFactory


def run():
    for _ in range(500):
        user = UserFactory()
        user.save()
        house = HouseFactory(user=user)
        house.save()
        for _ in range(5):
            ExpenseFactory(house=house, month=random.randint(1, 12)).save()
