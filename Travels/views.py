from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from Travels.models import BusDet
from Travels.forms import TicketForm

def index(request):
    context=BusDet.objects.all()
    return render(request,'HomeTick.html',{'context':context})

def BookTickets(request):
    l1=[]
    form=TicketForm()
    if request.method=="POST":
        form=TicketForm(request.POST)
        if form.is_valid():
            busno=form.cleaned_data['busno']
            Destinations=form.cleaned_data['Destinations']
            nopersons=form.cleaned_data['nopersons']
            b=BusDet.objects.get(busno=busno)
            l1=b.Destinations.split(',')
            for Destinations in l1:
                if b.Seatsavail>=nopersons:
                    b.Seatsavail=b.Seatsavail-nopersons
                    b.save()
                    return HttpResponse('Tickets are booked')
                else:
                    return HttpResponse('Tickets are not booked')
    return render(request,'BookTickets.html',{'form':form})
                