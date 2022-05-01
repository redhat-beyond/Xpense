import pytest
from django.contrib.auth.models import User

from expenses.models import Expenses
from house.models import House
from scripts.create_mock_data import run


@pytest.mark.django_db()
class TestScripts:
    def test_create_mock_data(self):
        mock_num_for_test = 10
        run(mock_num_for_test)
        assert len(User.objects.all()) == mock_num_for_test
        assert len(House.objects.all()) == mock_num_for_test
        assert len(Expenses.objects.all()) == mock_num_for_test * 5
