from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from Grocerystore.models import Grocery
from Grocerystore.forms import GroceryForm

def index(request):
    context=Grocery.objects.all()
    return render(request,'grochome.html',{'context':context})

def additem(request):
    form=GroceryForm()
    if request.method=='POST':
        form=GroceryForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            type=form.cleaned_data['type']
            qty=int(form.cleaned_data['qty'])
            Rpu=float(form.cleaned_data['Rpu'])
            amount=int(qty)*float(Rpu)
            gr=Grocery(name=name,type=type,qty=qty,Rpu=Rpu,amount=amount)
            gr.save()
            return HttpResponseRedirect('../displaygrocery')
    return render(request,'additem.html',{'form':form})

def displaygrocery(request):
    context=Grocery.objects.all()
    return render(request,'displaygrocery.html',{'context':context})