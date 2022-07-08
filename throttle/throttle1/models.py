
from unicodedata import name
from django.db import models


class Custom(models.Model):
    name = models.CharField(max_length=20, blank=True)
    roll = models.IntegerField( blank=True)
    city = models.CharField(max_length=50, blank=True)

class Owner(models.Model):
    name = models.CharField(max_length=20, blank=True)
    cust_name=models.ForeignKey(Custom,on_delete=models.CASCADE,related_name='ownby')