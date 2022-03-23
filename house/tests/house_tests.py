import pytest
from house.models import House, City, Country


@pytest.fixture
def generate_country():
    """
    Generates a Country object.
    """
    return Country.create_country(name="Israel")


@pytest.fixture
def generate_city(generate_country):
    """
    Generates a City object.
    """
    return City.create_city(name="Tel-Aviv", country=generate_country)


@pytest.fixture
def generate_house(generate_country, generate_city, house_id=1, name="House",
                   public=True, parent_profession_1="Teacher",
                   parent_profession_2="Student", income=1000, children=2):
    house = House.create_house(house_id=house_id,
                               name=name,
                               public=public,
                               country=generate_country,
                               city=generate_city,
                               parent_profession_1=parent_profession_1,
                               parent_profession_2=parent_profession_2,
                               income=income,
                               children=children)
    house.save()
    return house


@pytest.mark.django_db
class TestCourseModel:
    def test_create_house(self, generate_house):
        assert House.objects.get(
            house_id=generate_house.house_id) == generate_house
