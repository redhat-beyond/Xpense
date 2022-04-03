# from django.shortcuts import render
from django.views.generic import TemplateView
from house.models import Country, House, City
from django.shortcuts import render


def welcome_page(request):
    return render(request, 'home.html')


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


class ChartView(TemplateView):
    template_name = 'chart.html'
