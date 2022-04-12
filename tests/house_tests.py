import pytest
from house.models import House


@pytest.mark.django_db
class TestHouseModel:
    def test_save_house(self, generate_house):
        generate_house.save()
        assert generate_house in House.objects.all()

    def test_delete_house(self, generate_house):
        generate_house.save()
        generate_house.delete()
        assert generate_house not in House.objects.all()
