from django import forms
from Foodstore.models import FoodItem

ch=(('vegetable','1'),('fruits','2'),('nuts','3'))

class FoodForm(forms.Form):
    vname=forms.CharField(max_length=200)
    vegtype=forms.ChoiceField(choices=ch)
    vitamin=forms.CharField(max_length=200)

