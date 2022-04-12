from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.db.models import Avg, IntegerField, Q
from django.db.models.query import QuerySet

from house.constants import GLOBAL_PAGE
from house.forms import HouseForm
from house.models import Country, House, City
from expenses.models import Expenses


def home_page(request):
    return render(request, "home.html")


def filter_houses_by_form(form: HouseForm, all_houses: QuerySet[House]):
    if form.is_valid():
        cd = form.cleaned_data
        for key, value in cd.items():
            if value is not None and value != '':
                if 'profession' in key and cd['parent_profession_1'] != cd['parent_profession_2']:
                    all_houses = all_houses.filter(Q(parent_profession_1=value) | Q(parent_profession_2=value))
                else:
                    all_houses = all_houses.filter(**{key: value})

    return all_houses


def average_expenses_of_houses_by_categories(houses):
    return (
        Expenses.objects.filter(house_name__name__in=houses.values_list('name'))
        .order_by()
        .values('category')
        .annotate(average=Avg("amount", output_field=IntegerField()))
    )


def global_page(request):
    houses = House.objects.all()

    if request.method == 'POST':
        form = HouseForm(request.POST)
        houses = filter_houses_by_form(form, houses)
    else:
        form = HouseForm()

    categories_amounts = average_expenses_of_houses_by_categories(houses)
    context = {
        'all_houses': houses,
        "categories": [category.get('category') for category in categories_amounts],
        "amounts": [amount.get('average') for amount in categories_amounts],
        "form": form,
    }
    return render(request, GLOBAL_PAGE, context)


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'global/city_dropdown.html', {'cities': cities})


def house_login(request):
    return HttpResponse('house login')


def house_view(request, house_id):
    return HttpResponse(f'this is the house view for house {house_id}')


def add_house(request):
    post = request.POST["id"]
    return HttpResponse(f"try to update data for house POST PARAMETERS {'None' if post is None else post}")
