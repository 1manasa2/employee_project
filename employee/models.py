from django.db import models

# Create your models here.
class Employee(models.Model):
    empnum=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=30)
    empsalary=models.IntegerField()
    empAddress=models.CharField(max_length=200)
    def __str__(self):
        return str(self.empnum)+"--->"+self.empname