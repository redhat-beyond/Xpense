import random
from factories.expense import ExpenseFactory
from factories.house import HouseFactory


def run():
    for _ in range(500):
        house = HouseFactory()
        for _ in range(5):
            ExpenseFactory(house=house, month=random.randint(1, 12)).save()
        house.save()
