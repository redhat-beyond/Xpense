from django import forms
from expenses.models import Expenses
from house.models import House, Job
from datetime import datetime


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('country', 'city', 'children')

    jobs = Job.choices.copy()
    jobs.append((None, '---------'))
    parent_profession_1 = forms.ChoiceField(choices=jobs, required=False)
    parent_profession_2 = forms.ChoiceField(choices=jobs, required=False)
    highest_income = forms.IntegerField(label='highest income', required=False)
    lowest_income = forms.IntegerField(label='lowest income', required=False)

    def __init__(self, *args, **kwargs):
        super(HouseForm, self).__init__(*args, **kwargs)
        self.fields['country'].required = False
        self.fields['city'].required = False
        self.fields['children'].required = False


class HouseCreationForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('name', 'country', 'city')

    parent_profession_1 = forms.ChoiceField(choices=Job.choices, required=True)
    parent_profession_2 = forms.ChoiceField(choices=Job.choices, required=True)
    income = forms.IntegerField(label='Monthly Income', required=True, min_value=0)
    children = forms.IntegerField(label='Number of Children', required=True, min_value=0, max_value=20)
    public = forms.BooleanField(label='public', required=False, initial=True)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('date', 'amount', 'category', 'description')


def get_current_year():
    return datetime.now().year


def get_list_of_relevant_years():
    return [(y, y) for y in reversed(range(2020, (get_current_year() + 1)))]


class YearFilterForm(forms.Form):
    list_of_relevant_years = get_list_of_relevant_years()
    year = forms.ChoiceField(
        choices=list_of_relevant_years,
        required=False,
        initial=get_current_year(),
        widget=forms.Select(attrs={'onchange': 'form.submit();'}),
    )
