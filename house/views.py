from django.shortcuts import render
from house.constants import HOME_PAGE_ROUTE, GLOBAL_PAGE_ROUTE, HOUSE_LOGIN_ROUTE


def home_page(request):
    return render(request, HOME_PAGE_ROUTE)


def global_page(request):
    return render(request, GLOBAL_PAGE_ROUTE)


def house_login(request):
    return render(request, HOUSE_LOGIN_ROUTE)


def house_view(request, house_id):
    raise NotImplementedError


def add_house(request):
    raise NotImplementedError
