from django import forms
from .models import Employee


class Employee_form(forms.Form):
    empnum=forms.IntegerField()
    empname=forms.CharField(max_length=200)
    empsalary=forms.IntegerField()
    empAddress=forms.CharField(max_length=200)

class EmpForm(forms.Form):
    empsalary=forms.IntegerField()
    empnum=forms.IntegerField()