from django.db import models

# Create your models here.

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField(max_length=200)

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    company = models.CharField(max_length=200)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=200)
    pcategory = models.CharField(max_length=200)
    pquantity = models.IntegerField()
    pprice = models.IntegerField()
    sid = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    quantity = models.IntegerField()
    paid_amount = models.IntegerField()
    status = models.CharField(max_length=200)

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    quantity = models.IntegerField()
    status = models.CharField(max_length=200)

