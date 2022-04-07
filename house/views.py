from django.http import HttpResponse
from house.forms import HouseForm
from house.models import Country, House, City
from expenses.models import Expenses
from django.shortcuts import render, redirect
from django.db.models import Avg, IntegerField
from django.utils import timezone
from django.db.models import Q


def home_page(request):
    return render(request, "home.html")


def global_page(request):
    all_houses = House.objects.all()

    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key, value in cd.items():
                if value is not None and value != '':
                    if 'profession' in key and cd['parent_profession_1'] != cd['parent_profession_2']:
                        all_houses = all_houses.filter(Q(parent_profession_1=value) | Q(parent_profession_2=value))
                    else:
                        all_houses = all_houses.filter(**{key: value})
    else:
        form = HouseForm()

    categories_amounts = (
        Expenses.objects.filter(house_name__name__in=all_houses.values_list('name'))
        .order_by()
        .values('category')
        .annotate(total=Avg("amount", output_field=IntegerField()))
    )

    context = {
        'all_houses': all_houses,
        "categories": [category.get('category') for category in categories_amounts],
        "amounts": [amount.get('total') for amount in categories_amounts],
        "form": form,
    }
    return render(request, 'global/global.html', context)


def load_cities(request):
    country_id = request.GET.get('country')
    print(country_id)
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'global/city_dropdown.html', {'cities': cities})


def house_login(request):
    return HttpResponse('house login')


def house_view(request, house_id):
    return HttpResponse(f'this is the house view for house {house_id}')


def add_house(request):
    post = request.POST["id"]
    return HttpResponse(f"try to update data for house POST PARAMETERS {'None' if post is None else post}")


def house_form(request):
    submitted = False
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            # assert False
            return redirect('/global?submitted=True')
    else:
        form = HouseForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'global.html', {'form': form, 'submitted': submitted})
