from expenses.models import Expenses


def run():
    for expense in Expenses.objects.all():
        print(f"{expense.description}, {expense.house_name}, {expense.category}, {expense.amount}, {expense.date}")
