import pytest

from factories.house import HouseFactory
from house.helpers import _filter_houses_by_form
from house.models import House, City, Country, Job

HOUSE_NAME = "House 1"
HOUSE_PUBLIC = True
COUNTRY = "Colorado"
CITY = "South Park"
HOUSE_PARENT_PROFESSION_1 = "Teacher"
HOUSE_PARENT_PROFESSION_2 = "Student"
HOUSE_INCOME = 10_000
HOUSE_CHILDREN = 1


@pytest.fixture
def generate_country():
    return Country.create_country(name=COUNTRY)


@pytest.fixture
def generate_city(generate_country):
    return City.create_city(name=CITY, country=generate_country)


@pytest.fixture
def generate_house(generate_country, generate_city):
    house = House.create_house(
        name=HOUSE_NAME,
        public=HOUSE_PUBLIC,
        country=generate_country,
        city=generate_city,
        parent_profession_1=HOUSE_PARENT_PROFESSION_1,
        parent_profession_2=HOUSE_PARENT_PROFESSION_2,
        income=HOUSE_INCOME,
        children=HOUSE_CHILDREN,
    )
    return house


@pytest.mark.django_db
class TestHouseModel:
    def test_create_house(self, generate_house):
        assert (
                generate_house.name == HOUSE_NAME
                and generate_house.public == HOUSE_PUBLIC
                and generate_house.country.name == COUNTRY
                and generate_house.city.name == CITY
                and generate_house.parent_profession_1 == HOUSE_PARENT_PROFESSION_1
                and generate_house.parent_profession_2 == HOUSE_PARENT_PROFESSION_2
                and generate_house.income == HOUSE_INCOME
                and generate_house.children == HOUSE_CHILDREN
        )

    def test_save_house(self, generate_house):
        generate_house.save()
        assert generate_house in House.objects.all()

    def test_delete_house(self, generate_house):
        generate_house.save()
        generate_house.delete()
        assert generate_house not in House.objects.all()


@pytest.mark.django_db
class TestFilterHouseForm:

    def test_filter_parent_profession_1(self):
        pass_filter_house_create()
        HouseFactory(country=Country.objects.get(name='Israel'), city=City.objects.get(name='Tel Aviv'), income=5000,
                     children=1, parent_profession_1=Job.OTHER).save()
        houses = _filter_houses_by_form(form_data_filter_tests(), House.objects.all())
        assert len(houses) == 1

    def test_filter_country(self):
        pass_filter_house_create()
        HouseFactory(country=Country.objects.get(name='India'), city=City.objects.get(name='Tel Aviv'), income=5000,
                     children=1, parent_profession_1=Job.TEACHER).save()
        houses = _filter_houses_by_form(form_data_filter_tests(), House.objects.all())
        assert len(houses) == 1

    def test_filter_city(self):
        pass_filter_house_create()
        HouseFactory(country=Country.objects.get(name='Israel'), city=City.objects.get(name='Ramat Gan'), income=5000,
                     children=1, parent_profession_1=Job.TEACHER).save()
        houses = _filter_houses_by_form(form_data_filter_tests(), House.objects.all())
        assert len(houses) == 1

    def test_filter_highest_income(self):
        pass_filter_house_create()
        HouseFactory(country=Country.objects.get(name='Israel'), city=City.objects.get(name='Tel Aviv'), income=12000,
                     children=1, parent_profession_1=Job.TEACHER).save()
        houses = _filter_houses_by_form(form_data_filter_tests(), House.objects.all())
        assert len(houses) == 1

    def test_filter_lowest_income(self):
        pass_filter_house_create()
        HouseFactory(country=Country.objects.get(name='Israel'), city=City.objects.get(name='Tel Aviv'), income=4000,
                     children=1, parent_profession_1=Job.TEACHER).save()
        houses = _filter_houses_by_form(form_data_filter_tests(), House.objects.all())
        assert len(houses) == 1


def pass_filter_house_create():
    HouseFactory(country=Country.objects.get(name='Israel'), city=City.objects.get(name='Tel Aviv'), income=5000,
                 children=1, parent_profession_1=Job.TEACHER).save()


def form_data_filter_tests():
    return {
        'country': Country.objects.get(name='Israel'),
        'city': City.objects.get(name='Tel Aviv'),
        'parent_profession_1': HOUSE_PARENT_PROFESSION_1,
        'parent_profession_2': None,
        'highest_income': 10000,
        'lowest_income': 5000,
        'children': 1,
    }
