from django.db import models

# Create your models here.
class Bidding(models.Model):
    bidid = models.AutoField(primary_key=True)
    productid= models.IntegerField()
    uid = models.CharField(max_length=50)
    bidprice = models.IntegerField()
    info= models.CharField(max_length=100)
