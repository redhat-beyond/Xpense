import pytest
from django.utils import timezone
from story.models import Story
from house.models import House, Country, City

TEMP_DATE = timezone.now()
TEMP_STORY = "This is my story"

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


@pytest.fixture
def generate_story(generate_house):
    return Story.create_story(house_ID=generate_house, last_edited=TEMP_DATE, text=TEMP_STORY)


@pytest.mark.django_db()
class TestStoryModel:
    def test_new_story(self, generate_story):
        assert generate_story.last_edited == TEMP_DATE
        assert generate_story.text == TEMP_STORY

    def test_persist_story(self, generate_story):
        generate_story.save()
        assert generate_story in Story.objects.all()

    def test_story_is_deleted_after_house_was_deleted(self, generate_story):
        generate_story.save()
        generate_story.house_ID.delete()

        assert generate_story not in Story.objects.all()
