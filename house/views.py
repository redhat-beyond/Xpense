from house.constants import MINE_MINE_PAGE_ROUTE
from django.shortcuts import render, get_object_or_404
from house.constants import HOME_PAGE_ROUTE, GLOBAL_PAGE_ROUTE, GLOBAL_PAGE_CITY_DROPDOWN_ROUTE, LOGIN_PAGE_ROUTE
from .forms import HouseForm, HouseIDForm
from .helpers import _filter_houses_by_form
from expenses.models import Expenses
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from .models import House, City


def home_page(request):
    return render(request, HOME_PAGE_ROUTE)


def global_page(request):
    houses = House.objects.all()
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            houses = _filter_houses_by_form(cleaned_data, houses)
    else:
        form = HouseForm()

    categories_amounts = Expenses.average_expenses_of_houses_by_categories(houses)
    context = {
        'all_houses': houses,
        "categories": [category.get('category') for category in categories_amounts],
        "amounts": [amount.get('average') for amount in categories_amounts],
        "form": form,
    }
    return render(request, GLOBAL_PAGE_ROUTE, context)


def house_login(request):
    errorMsg = ""

    if request.method == 'POST':
        try:
            form = HouseIDForm(request.POST)
            house_id = form.data["house_id"]

            if House.objects.filter(house_id=house_id).count() == 1:
                return HttpResponseRedirect(f'/../house/{house_id}')
            else:
                errorMsg = "There is no House with the provided ID"
                form = HouseIDForm()
        # In case an exception not a valid UUID is thrown
        except ValidationError:
            errorMsg = "There is no House with the provided ID : " + house_id
            form = HouseIDForm()
    else:
        form = HouseIDForm()

    return render(request, LOGIN_PAGE_ROUTE, {'form': form, 'msg': errorMsg})


def house_view(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    expenses_list = Expenses.objects.filter(house_name=house)
    context = {'house': house,
               'house_expenses': expenses_list}
    return render(request, MINE_MINE_PAGE_ROUTE, context)


def add_house(request):
    raise NotImplementedError


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    context = {'cities': cities}
    return render(request, GLOBAL_PAGE_CITY_DROPDOWN_ROUTE, context)
