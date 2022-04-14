from house.constants import HOME_PAGE_ROUTE, GLOBAL_PAGE_ROUTE
from .models import House
from django.shortcuts import render


def home_page(request):
    # this line is needed till the login of the mine page will create and merge
    print(House.objects.all().order_by("?").first().house_id)
    return render(request, HOME_PAGE_ROUTE)


def global_page(request):
    context = {'all_houses': House.objects.all()}
    return render(request, GLOBAL_PAGE_ROUTE, context)


def house_login(request):
    raise NotImplementedError


def house_view(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    expenses_list = Expenses.objects.filter(house_name=house)
    context = {'house': house,
               'house_expenses': expenses_list}
    return render(request, HOUSE_PAGE_ROUTE, context)


def add_house(request):
    raise NotImplementedError
