import random
from factories.expense import ExpenseFactory
from factories.house import HouseFactory
from factories.user import UserFactory


def run(*args):
    if args:
        number_to_create = int(args[0])
    else:
        print("Please provide a number of records to create.\n"
              "Example: manage.py runscript create_mock_data --script-args 10.")
        return
    print(f"Creating {number_to_create} users with mock data")
    for _ in range(number_to_create):
        user = UserFactory()
        user.save()
        house = HouseFactory(user=user)
        house.save()
        for _ in range(5):
            ExpenseFactory(house=house, month=random.randint(1, 12)).save()
