from django import forms
from .models import BusDet
class TicketForm(forms.Form):
    busno=forms.IntegerField()
    Destinations=forms.CharField()
    nopersons=forms.IntegerField()