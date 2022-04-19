from expenses.models import Expenses
from house.constants import HOME_PAGE_ROUTE, GLOBAL_PAGE_ROUTE
from .models import House
from django.shortcuts import render


def home_page(request):
    return render(request, HOME_PAGE_ROUTE)


def global_page(request):
    houses = House.objects.all()
    categories_amounts = Expenses.average_expenses_of_houses_by_categories(houses)
    context = {
        'all_houses': houses,
        "categories": [category.get('category') for category in categories_amounts],
        "amounts": [amount.get('average') for amount in categories_amounts],
    }
    return render(request, GLOBAL_PAGE_ROUTE, context)


def house_login(request):
    raise NotImplementedError


def house_view(request, house_id):
    raise NotImplementedError


def add_house(request):
    raise NotImplementedError
