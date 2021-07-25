from django.db import models

class Category(models.Model):
    catid = models.AutoField(primary_key=True)
    catname = models.CharField(max_length=50)
    caticonname= models.CharField(max_length=50)

class Subcategory(models.Model):
    subcatid = models.AutoField(primary_key=True)
    catid = models.IntegerField()
    subcatname = models.CharField(max_length=50)
    subcaticonname= models.CharField(max_length=50)

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    title= models.CharField(max_length=50)
    catid = models.IntegerField()
    subcatid = models.IntegerField()
    pdescription = models.CharField(max_length=150)
    bprice= models.IntegerField()
    piconname=models.CharField(max_length=100)
    info=models.CharField(max_length=100)

    # def __str__(self):
    #     return self.product_name