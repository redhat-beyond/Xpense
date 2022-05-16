from house.constants import MINE_ADD_EXPENSE_ROUTE
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from expenses.models import Expenses
from house.constants import HOME_PAGE_ROUTE, GLOBAL_PAGE_ROUTE, GLOBAL_PAGE_CITY_DROPDOWN_ROUTE, \
    MINE_MINE_PAGE_ROUTE, HOUSE_CREATE_ROUTE
from .forms import HouseForm, HouseCreationForm, ExpenseForm
from .models import House, City
from .helpers import _filter_houses_by_form


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


@login_required
def house_view(request):
    user = request.user
    if hasattr(user, 'house') is False:
        return HttpResponseRedirect('/../house_create')

    house = user.house
    expenses_list = Expenses.objects.filter(house_name=house)
    context = {'house': house, 'house_expenses': expenses_list}
    return render(request, MINE_MINE_PAGE_ROUTE, context)


def add_house(request):
    raise NotImplementedError


@login_required
def add_expense(request):
    errorMsg = ""
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            user = request.user
            house = user.house
            Expenses.create_expense(
                house_name=house,
                amount=expense_form.data['amount'],
                date=expense_form.data['date'],
                category=expense_form.data['category'],
                description=expense_form.data['description'],
            )
            return HttpResponseRedirect('/../house')
    else:
        expense_form = ExpenseForm()
    return render(request, MINE_ADD_EXPENSE_ROUTE, {'form': expense_form, 'msg': errorMsg})


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    context = {'cities': cities}
    return render(request, GLOBAL_PAGE_CITY_DROPDOWN_ROUTE, context)


@login_required
def house_create(request):
    errorMsg = ""
    if request.method == 'POST':
        house_form = HouseCreationForm(request.POST)
        if house_form.is_valid():
            cleaned_data = house_form.cleaned_data
            House.create_house(user=request.user,
                               name=cleaned_data['name'],
                               public=cleaned_data['public'],
                               parent_profession_1=cleaned_data['parent_profession_1'],
                               parent_profession_2=cleaned_data['parent_profession_2'],
                               country=cleaned_data['country'],
                               city=cleaned_data['city'],
                               children=cleaned_data['children'],
                               income=cleaned_data['income'])
            return HttpResponseRedirect('/../house')
    else:
        house_form = HouseCreationForm()

    return render(request, HOUSE_CREATE_ROUTE, {'form': house_form, 'msg': errorMsg})
