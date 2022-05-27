from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from expenses.models import Expenses
from house.constants import (
    HOME_PAGE_ROUTE,
    GLOBAL_PAGE_ROUTE,
    MINE_PAGE_ROUTE,
    HOUSE_CREATE_ROUTE,
    MINE_ADD_EXPENSE_ROUTE,
    MINE_EDIT_EXPENSE_ROUTE,
    BY_MONTH,
    MONTHS,
)
from .forms import HouseForm, HouseCreationForm, ExpenseForm, YearFilterForm
from .models import House
from .helpers import _filter_houses_by_form
from django.db.models import Sum
from datetime import datetime


def home_page(request):
    return render(request, HOME_PAGE_ROUTE)


def global_page(request):
    houses = House.objects.filter(public=True)
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
        'categories': [category.get('category') for category in categories_amounts],
        'amounts': [amount.get('average') for amount in categories_amounts],
        'form': form,
    }
    return render(request, GLOBAL_PAGE_ROUTE, context)


@login_required
def house_view(request):
    user = request.user
    if hasattr(user, 'house') is False:
        return HttpResponseRedirect('/../house_create')

    house = user.house
    expenses_list = Expenses.objects.filter(house_name=house)

    if request.method == 'POST':
        form = YearFilterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            expenses_list = expenses_list.filter(date__year=cleaned_data['year'])
    else:
        form = YearFilterForm()
        current_year = datetime.now().year
        expenses_list = expenses_list.filter(date__year=current_year)

    expenses_sum_by_month = expenses_list.values(BY_MONTH).annotate(sum=Sum('amount'))
    categories = MONTHS

    context = {
        'form': form,
        'house': house,
        'house_expenses': expenses_list,
        'categories': [categories[amount.get(BY_MONTH) - 1] for amount in expenses_sum_by_month],
        'amounts': [amount.get('sum') for amount in expenses_sum_by_month],
    }
    return render(request, MINE_PAGE_ROUTE, context)


@login_required
def add_expense(request):
    error_message = ''
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
    return render(request, MINE_ADD_EXPENSE_ROUTE, {'form': expense_form, 'msg': error_message})


@login_required
def house_create(request):
    error_message = ''
    if request.method == 'POST':
        house_form = HouseCreationForm(request.POST)
        if house_form.is_valid():
            cleaned_data = house_form.cleaned_data
            House.create_house(
                user=request.user,
                name=cleaned_data['name'],
                public=cleaned_data['public'],
                parent_profession_1=cleaned_data['parent_profession_1'],
                parent_profession_2=cleaned_data['parent_profession_2'],
                country=cleaned_data['country'],
                city=cleaned_data['city'],
                children=cleaned_data['children'],
                income=cleaned_data['income'],
            )
            return HttpResponseRedirect('/../house')
    else:
        house_form = HouseCreationForm()

    return render(request, HOUSE_CREATE_ROUTE, {'form': house_form, 'msg': error_message})


@login_required
def edit_expense(request, id):
    user = request.user
    house = user.house
    expenses_list = Expenses.objects.filter(house_name=house)
    expense = get_object_or_404(Expenses, pk=id)
    if expense not in expenses_list:
        request.status_code = 400
        return request
    form = ExpenseForm(request.POST or None, instance=expense)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            return HttpResponseRedirect('/../house')
    else:
        return render(request, MINE_EDIT_EXPENSE_ROUTE, context)


@login_required
def delete_expense(request, id):
    user = request.user
    house = user.house
    expenses_list = Expenses.objects.filter(house_name=house)
    expense = get_object_or_404(Expenses, pk=id)
    if expense not in expenses_list:
        request.status_code = 400
        return request
    expense.delete()
    return HttpResponseRedirect('/../house')
