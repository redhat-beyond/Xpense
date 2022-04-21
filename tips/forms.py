from django import forms
from .models import Tip


class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ('author', 'text', 'category')
