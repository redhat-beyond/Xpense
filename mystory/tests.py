import pytest
from django.utils import timezone
from mystory.models import MyStory
from house.models import House, Country, City

TEMP_DATE = timezone.now()
TEMP_STORY = "This is my story"

HOUSE_NAME = "House 1"
HOUSE_PUBLIC = True
COUNTRY = "Colorado"
CITY = "South Park"
HOUSE_PARENT_PROFESSION_1 = "Teacher"
HOUSE_PARENT_PROFESSION_2 = "Student"
country = Country(name=COUNTRY)
city = City(name=CITY, country=country)
house = House(name=HOUSE_NAME, public=HOUSE_PUBLIC, country=country, city=city, income=1, children=1)


@pytest.mark.django_db()
def test_new_item():
    country.save()
    city.save()
    house.save()
    item = MyStory(story_date=TEMP_DATE, story_text=TEMP_STORY, house=house)
    item.save()

    assert item.story_text == TEMP_STORY
    assert item.story_date == TEMP_DATE
    assert item.house.house_id == house.house_id


@pytest.fixture
def story0():
    return MyStory(story_date=TEMP_DATE, story_text=TEMP_STORY, house=house)


class TestMystoryModel:
    def test_new_story(self, story0):
        assert story0.story_date == TEMP_DATE
        assert story0.story_text == TEMP_STORY

    @pytest.mark.django_db()
    def test_persist_story(self, story0):
        country.save()
        city.save()
        house.save()
        story0.save()

        assert story0 in MyStory.objects.all()

    @pytest.mark.django_db()
    def test_deletecascade_house(self, story0):
        country.save()
        city.save()
        house.save()
        story0.save()
        house.delete()

        assert story0 not in MyStory.objects.all()
