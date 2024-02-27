from django.db import models
ch=(('1','Standard'),('2','Classic'),('3','Deluxe'))
# Create your models here.

class Rooms(models.Model):
    Roomtype=models.CharField(max_length=200,choices=ch)
    Availablecount=models.IntegerField()
    Rpu=models.IntegerField()
    def __str__(self):
        return self.Roomtype+'-'+str(self.Availablecount)
