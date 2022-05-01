from django import forms

from house.models import House, Job, Country, City


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


class HouseCreationForm(forms.Form):
    name = forms.CharField(label='House Name', required=True)
    parent_profession_1 = forms.ChoiceField(choices=Job.choices, required=True)
    parent_profession_2 = forms.ChoiceField(choices=Job.choices, required=True)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=True)
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    income = forms.IntegerField(label='Monthly Income', required=True, min_value=0)
    children = forms.IntegerField(label='Number of Children', required=True, min_value=0, max_value=20)
    public = forms.BooleanField(label='public', required=False, initial=True)
