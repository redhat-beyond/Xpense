<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import render
from house.constants import HOME_PAGE_ROUTE, GLOBAL_PAGE_ROUTE


=======
>>>>>>> 2bd9f3f (init routing)
=======
from django.shortcuts import render
from house.constants import HOME_PAGE_ROUTE


>>>>>>> 31ddc69 (Create home and base html initial code)
def home_page(request):
    return render(request, HOME_PAGE_ROUTE)


def global_page(request):
    return render(request, GLOBAL_PAGE_ROUTE)


def house_login(request):
    raise NotImplementedError


def house_view(request, house_id):
    raise NotImplementedError


def add_house(request):
    raise NotImplementedError
