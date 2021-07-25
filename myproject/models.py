from django.db import models

class Register(models.Model):
    regid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username= models.CharField(max_length=50)
    password= models.CharField(max_length=10)
    mobile= models.CharField(max_length=12)
    address= models.CharField(max_length=1000)
    city= models.CharField(max_length=20)
    gender= models.CharField(max_length=10)
    role= models.CharField(max_length=10)
    status= models.IntegerField()
    info= models.CharField(max_length=100)

class Contact(models.Model):
    name=models.CharField(max_length=15)
    number=models.CharField(max_length=50)
    email=models.CharField(max_length=15)
    message=models.CharField(max_length=500)

    # def __str__(self):
    #     return self.product_name