from django import forms
from house.models import House, Job


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


class HouseIDForm(forms.Form):
    house_id = forms.UUIDField(label='Enter Your House ID')
