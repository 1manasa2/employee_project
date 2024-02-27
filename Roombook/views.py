from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from Roombook.models import Rooms
from Roombook.forms import BookForm
from Roombook.forms import ChoiceForm

def index(request):
    context=Rooms.objects.all()
    return render(request,'RoomHome.html',{'context':context})

def addRooms(request):
    form=BookForm()
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            Roomtype=form.cleaned_data['Roomtype']
            Availablecount=form.cleaned_data['Availablecount']
            Rpu=form.cleaned_data['Rpu']
            r=Rooms(Roomtype=Roomtype,Availablecount=Availablecount,Rpu=Rpu)
            r.save()
            return HttpResponseRedirect('../disproomdet')
    return render(request,'addRooms.html',{'form':form})

def BookRoom(request):
    form1=ChoiceForm()
    if request.method=="POST":
        form1=ChoiceForm(request.POST)
        if form1.is_valid():
            Roomtype=form1.cleaned_data['Roomtype']
            Roomcount=form1.cleaned_data['Roomcount']
            r=Rooms.objects.get(Roomtype=Roomtype)
            if r.Availablecount >= Roomcount:
                r.Availablecount=r.Availablecount-Roomcount
                r.save()
                return HttpResponse(f'{Roomcount} of type {Roomtype} are booked')
            else:
                return HttpResponse('Booking Failed')
    return render(request,'BookRoom.html',{'form1':form1})

def disproomdet(request):
    context=Rooms.objects.all()
    return render(request,'disproomdet.html',{'context':context})
