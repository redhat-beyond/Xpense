from django import forms
from expenses.models import Expenses


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('date', 'amount', 'category', 'description')
