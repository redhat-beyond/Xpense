from django.http import HttpResponseRedirect
from django.shortcuts import render
from urllib3 import HTTPResponse
from house.constants import HOME_PAGE_ROUTE, GLOBAL_PAGE_ROUTE, LOGIN_PAGE_ROUTE

from house.forms import HouseIdForm
from house.models import House
# import house ??


def home_page(request):
    return render(request, HOME_PAGE_ROUTE)


def global_page(request):
    return render(request, GLOBAL_PAGE_ROUTE)


def house_login(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = HouseIdForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            house_id = form.data["house_id"]

        # if User.objects.filter(email=cleaned_info['username']).exists():
        #    return HttpResponseRedirect(reverse(LOGIN_PAGE_ROUTE))
        if House.objects.filter(house_id=house_id).exists():

            return HttpResponseRedirect('/../{house_id}')
        # ////// OR //////
        # if House.objects.get(house_id=house_id):
        #    return HttpResponseRedirect('/../{house_id}')

        else:
            # Create a new House with the given house_id:

            House.objects.create(house_id=house_id)
            print("House created with id: " + house_id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HouseIdForm()

    return render(request, LOGIN_PAGE_ROUTE, {'form': form})


def house_view(request, house_id):
    raise NotImplementedError


def add_house(request):
    raise NotImplementedError
