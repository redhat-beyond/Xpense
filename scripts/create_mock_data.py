from factories.house import HouseFactory


def run():
    for i in range(500):
        HouseFactory().save()
