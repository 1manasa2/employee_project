from django import forms
from Roombook.models import Rooms
ch=(('1','Standard'),('2','Classic'),('3','Deluxe'))

class BookForm(forms.Form):
    Roomtype=forms.ChoiceField(choices=ch)
    Availablecount=forms.IntegerField()
    Rpu=forms.IntegerField()

class ChoiceForm(forms.Form):
    Roomtype=forms.ChoiceField(choices=ch)
    Roomcount=forms.IntegerField()
