from django.http import HttpResponse
from house.models import Country, House, City
from django.shortcuts import render


def home_page(request):
    return render(request, "home.html")


def global_page(request):
    country = Country.objects.get(name="Israel")
    House.create_house(
        'House 1',
        True,
        Country.objects.get(name="Israel"),
        City.objects.get(name="Tel Aviv", country=country),
        'Teacher',
        'Teacher',
        100,
        1,
    )
    all_houses = House.objects.all()
    context = {'all_houses': all_houses}
    return render(request, 'global.html', context)


def house_login(request):
    return HttpResponse('house login')


def house_view(request, house_id):
    return HttpResponse(f'this is the house view for house {house_id}')


def add_house(request):
    post = request.POST["id"]
    return HttpResponse(f"try to update data for house POST PARAMETERS {'None' if post is None else post}")
