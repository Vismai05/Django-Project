from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class myprd(models.Model):
    pid = models.AutoField
    pname = models.CharField(max_length=30)
    pcat = models.CharField(max_length=50)
    psubcat = models.CharField(max_length=60)
    pdes = models.CharField(max_length=120)
    pdate = models.DateField()
    pimg = models.ImageField(upload_to='shop/images')
    pcost = models.IntegerField()
    def __str__(self):
        return self.pname

class prdlist(models.Model):
    prd_id = models.AutoField
    prd_name = models.CharField(max_length=30)
    prd_cat = models.CharField(max_length=100)
    prd_subcat = models.CharField(max_length=100)
    prd_des = models.CharField(max_length=200)
    prd_date = models.DateField()
    prd_img = models.ImageField(upload_to='shop/images')
    prd_cost = models.IntegerField()
    def __str__(self):
        return self.prd_name

class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    mail = models.CharField(max_length=60)
    phone = models.IntegerField()
    message = models.CharField(max_length=600)
    def __str__(self):
        return "Sent By : "+self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items = models.CharField(max_length=8000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=40)
    phone = models.IntegerField()
    email = models.CharField(max_length=60)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,default="")
    country = models.CharField(max_length=80)
    state = models.CharField(max_length=120)
    pin = models.IntegerField()

class orderstatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    status = models.CharField(max_length=500)
    timestamp = models.DateField(auto_now_add=True)
