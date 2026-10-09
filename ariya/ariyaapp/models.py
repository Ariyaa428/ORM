from django.db import models
from django.contrib import admin 
class blinkit(models.Model):
        name=models.CharField(max_length=10)
        Address=models.TextField()
        Productname=models.CharField(max_length=10)
        Quantity=models.IntegerField
        price=models.IntegerField
        Mobile_Number=models.IntegerField(primary_key=True)
class blinkitadmin(admin.ModelAdmin):
      list_display=["name","Address","Productname","Quantity","price","Mobile_Number"]

