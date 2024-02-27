from django.db import models

# Create your models here.
class FoodItem(models.Model):
    vname=models.CharField(max_length=200)
    vegtype=models.CharField(max_length=200)
    vitamin=models.CharField(max_length=200)
    def __str__(self):
        return self.vname+'-'+self.vitamin