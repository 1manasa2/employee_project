from django import forms
from .models import Grocery

ch= (('oil','1'),('Grains','2'),('Cosmetics','3'))

class GroceryForm(forms.Form):
    name=forms.CharField(max_length=200)
    type=forms.ChoiceField(choices=ch)
    qty=forms.IntegerField()
    Rpu=forms.FloatField()
