from django.http import HttpResponse, HttpResponsePermanentRedirect,HttpResponseRedirect
from django.shortcuts import render,redirect
from employee.models import Employee
from employee.forms import Employee_form,EmpForm

class SalaryException(Exception):pass

def index(request):
    context=Employee.objects.all()
    return render(request,'home.html',{'context':context})

def display(request):
    context=Employee.objects.all()
    return render(request,'display.html',{'context':context})

def insert(request):
    form=Employee_form()
    flag=0
    if request.method=='POST':
        form=Employee_form(request.POST)
        if form.is_valid():
            empnum=int(form.cleaned_data['empnum'])
            empname=form.cleaned_data['empname']
            try:
                empsalary=int(form.cleaned_data['empsalary'])
                if empsalary<0:
                     flag=1
                     raise SalaryException
            except SalaryException:
                print("EXception raised")
            empAddress=form.cleaned_data['empAddress']
            if flag!=1:
                g=Employee(empnum,empname,empsalary,empAddress)
                g.save()
            return HttpResponseRedirect('../display')
    return render(request,'insert.html',{'form':form})

def update(request):
    form1=EmpForm()
    if request.method=="POST":
        form1=EmpForm(request.POST)
        if form1.is_valid():
            empnum=int(form1.cleaned_data['empnum'])
            empsalary=int(form1.cleaned_data['empsalary'])
            e=Employee.objects.get(empnum=empnum)
            e.empsalary=empsalary
            e.save()
            return HttpResponseRedirect('../display')
    return render(request,'update.html',{'form1':form1})

def delete(request):
    form1=EmpForm()
    if request.method=="POST":
        form1=EmpForm(request.POST)
        if form1.is_valid():
            empnum=int(form1.cleaned_data['empnum'])
            empsalary=int(form1.cleaned_data['empsalary'])
            emp=Employee.objects.get(empnum=empnum)
            emp.delete()
            return HttpResponseRedirect('../display')
    return render(request,'delete.html',{'form1':form1})

