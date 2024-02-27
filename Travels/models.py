from django.db import models

# Create your models here.

class BusDet(models.Model):
    busno=models.IntegerField()
    Departuretime=models.DurationField()
    Destinations=models.CharField(max_length=200)
    Seatsavail=models.IntegerField()
    Tickcost=models.IntegerField()
    def __str__(self):
        return str(self.busno)+'-->'+self.Destinations