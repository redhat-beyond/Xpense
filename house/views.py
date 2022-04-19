from house.constants import HOME_PAGE_ROUTE, GLOBAL_PAGE_ROUTE, GLOBAL_PAGE_CITY_DROPDOWN_ROUTE, HOUSE_CREATE_ROUTE
from .forms import HouseForm, HouseCreationForm
from .helpers import _filter_houses_by_form
from .models import House, City
from expenses.models import Expenses
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import ValidationError


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
    raise NotImplementedError


def house_view(request, house_id):
    raise NotImplementedError


def house_create(request):
    errorMsg = ""

    if request.method == 'POST':
        try:
            House_form = HouseCreationForm(request.POST)

            if House_form.is_valid():
                new_house = House_form.save()
                new_house_id = new_house.house_id
                return HttpResponseRedirect(f'/../{new_house_id}')
            else:
                errorMsg = "Invalid form data"
                return render(request, HOUSE_CREATE_ROUTE, {'form': House_form, 'msg': errorMsg})
        # In case an exception is thrown
        except ValidationError as ex:
            errorMsg = ex.message()
            House_form = HouseCreationForm()
    else:
        House_form = HouseCreationForm()

    return render(request, HOUSE_CREATE_ROUTE, {'form': House_form, 'msg': errorMsg})


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    context = {'cities': cities}
    return render(request, GLOBAL_PAGE_CITY_DROPDOWN_ROUTE, context)
