import pytest
from django.template.loader import get_template

from house.constants import USER_LOGIN_PAGE_ROUTE, USER_SIGNUP_ROUTE
from tests.const import USERNAME, PASSWORD, PASSWORD_NOT_MATCH


@pytest.mark.django_db()
class TestLoginPage:
    def test_user_login_template(self):
        get_template(USER_LOGIN_PAGE_ROUTE)

    def test_login_entry_point(self, client):
        response = client.get('/accounts/login/')
        assert response.status_code == 200
        assert 'registration/login.html' in response.template_name

    def test_login_user(self, client, new_user):
        response = client.post('/accounts/login/', {'username': USERNAME, 'password': PASSWORD})
        assert response.status_code == 302
        assert response.url == '/../house/'

    def test_bad_login(self, client):
        response = client.post('/accounts/login/', {'username': USERNAME, 'password': PASSWORD})
        assert response.status_code == 200
        assert 'registration/login.html' in response.template_name

    def test_logout_user(self, client, new_user):
        client.post('/accounts/login/', {'username': USERNAME, 'password': PASSWORD})
        response = client.get('/accounts/logout/')
        assert response.status_code == 302
        assert response.url == '/'


@pytest.mark.django_db()
class TestSignupPage:
    def test_signup_template(self):
        get_template(USER_SIGNUP_ROUTE)

    def test_signup_entry_point(self, client):
        response = client.get('/accounts/signup/')
        assert response.status_code == 200
        assert 'registration/signup.html' in response.template_name

    def test_signup_user(self, client):
        response = client.post('/accounts/signup/',
                               {'username': USERNAME, 'password1': PASSWORD, 'password2': PASSWORD})
        assert response.status_code == 302
        assert response.url == '/accounts/login/'

    def test_bad_signup(self, client):
        response = client.post('/accounts/signup/',
                               {'username': USERNAME, 'password1': PASSWORD, 'password2': PASSWORD_NOT_MATCH})
        assert response.status_code == 200
        assert 'registration/signup.html' in response.template_name

    def test_signup_login_flow(self, client):
        response = client.post('/accounts/signup/',
                               {'username': USERNAME, 'password1': PASSWORD, 'password2': PASSWORD})
        assert response.status_code == 302
        response = client.post('/accounts/login/', {'username': USERNAME, 'password': PASSWORD})
        assert response.status_code == 302
        assert response.url == '/../house/'
