from django.http import HttpResponseRedirect
from house.constants import HOME_PAGE_ROUTE, HOUSE_PAGE_ROUTE, GLOBAL_PAGE_ROUTE, ADD_EXPENSE_ROUST
from expenses.models import Expenses
from django.shortcuts import render, get_object_or_404
from .models import House
from .forms import ExpenseForm


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


def add_expense(request, house_id):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            house = House.objects.get(house_id=house_id)
            Expenses.create_expense(house_name=house, amount=form.data['amount'], date=form.data['date'],
                                    category=form.data['category'], description=form.data['description'])
            return HttpResponseRedirect(f'/../{house_id}')
    else:
        form = ExpenseForm()
    return render(request, ADD_EXPENSE_ROUST, {'form': form})


def add_house(request):
    raise NotImplementedError
