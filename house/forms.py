from django import forms


class HouseIdForm(forms.Form):
    house_id = forms.CharField(label='Enter Your House Id', max_length=100)
