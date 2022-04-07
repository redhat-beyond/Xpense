from factories.house import HouseFactory
from house.models import House, City, Country


def run():
    for house in House.objects.all():
        print(
            f"{house.name}, {house.country.name}, {house.city.name}, {house.income}, {house.children}, "
            + f"{house.parent_profession_1}, {house.parent_profession_2}"
        )
