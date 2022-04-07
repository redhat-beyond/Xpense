from expenses.models import Expenses
from factories.house import HouseFactory
from house.models import House, City, Country
from django.db.models import Sum


def run():
    # houses = House.objects.all()[:2].values_list('name', flat=True)
    houses = House.objects.all()[:2].values_list('name')
    print(houses)
    # categories_amounts = (
    #     Expenses.objects.filter(house_name__in=houses).order_by().values('category').annotate(total=Sum("amount"))
    # )
    categories_amounts = Expenses.objects.filter(house_name__name__in=houses)
    # print(categories_amounts)
    for expense in categories_amounts:
        print(f"{expense.description}, {expense.house_name}, {expense.category}, {expense.amount}, {expense.date}")
