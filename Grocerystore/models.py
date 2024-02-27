from django.db import models

# Create your models here.
class Grocery(models.Model):
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    qty=models.IntegerField()
    Rpu=models.FloatField()
    amount=models.IntegerField()
    def __str__(self):
        return self.name+'-->'+str(self.qty)
