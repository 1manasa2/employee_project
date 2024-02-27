from django.shortcuts import render,redirect

# Create your views here.

from Foodstore.models import FoodItem
from django.http import HttpResponse,HttpResponseRedirect
from Foodstore.forms import FoodForm

def index(request):
    context=FoodItem.objects.all()
    return render(request,'FoodHome.html',{'context':context})

def addfooditem(request):
    form=FoodForm()
    if request.method=="POST":
        form=FoodForm(request.POST)
        if form.is_valid():
            vname=form.cleaned_data['vname']
            vegtype=form.cleaned_data['vegtype']
            vitamin=form.cleaned_data['vitamin']
            f=FoodItem(vname=vname,vegtype=vegtype,vitamin=vitamin)
            f.save()
            return HttpResponseRedirect('../displayitems')
    return render(request,'addfooditem.html',{'form':form})

def displayitems(request):
    context=FoodItem.objects.all()
    return render(request,'displayitems.html',{'context':context})

