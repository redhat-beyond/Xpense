from factories.expense import ExpenseFactory


def run():
    for i in range(500):
        ExpenseFactory().save()
