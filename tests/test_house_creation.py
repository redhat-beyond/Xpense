import pytest

from house.models import House, Job


@pytest.mark.django_db()
class TestHouseCreation:
    def test_good_form(self, client, new_user):
        client.force_login(new_user)
        good_form_data = {'public': True, 'country': '1',
                          'city': '1', 'parent_profession_1': Job.OTHER,
                          'parent_profession_2': Job.OTHER, 'children': 2, 'income': 123, 'name': 'house name'}

        response = client.post('/house_create/', data=good_form_data)
        assert len(House.objects.all()) == 1
        assert response.status_code == 302
        assert response.url == '/../house'

    def test_bad_form(self, client, new_user):
        client.force_login(new_user)
        bad_form_data = {}
        response = client.post('/house_create/', data=bad_form_data)
        assert len(House.objects.all()) == 0
        assert response.status_code == 200
