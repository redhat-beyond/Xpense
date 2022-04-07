from django import forms
from house.models import Country, House, City, Job


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.initial['choices_field_name'] = 'default value'
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"
                bound_field.field.required = False


class HouseForm(BaseForm):
    class Meta:
        model = House
        fields = ('country', 'city', 'parent_profession_1', 'parent_profession_2', 'income', 'children')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['city'].queryset = City.objects.none()

        # if 'country' in self.data:
        #     try:
        #         country_id = int(self.data.get('country'))
        #         self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
