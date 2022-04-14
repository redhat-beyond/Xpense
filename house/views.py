from house.constants import HOME_PAGE_ROUTE, GLOBAL_PAGE_ROUTE
from .models import House
from django.shortcuts import render


def home_page(request):
    return render(request, HOME_PAGE_ROUTE)


def global_page(request):
    context = {'all_houses': House.objects.all()}
    return render(request, GLOBAL_PAGE_ROUTE, context)


def house_login(request):
    raise NotImplementedError


def house_view(request, house_id):
    raise NotImplementedError


def add_house(request):
    raise NotImplementedError
