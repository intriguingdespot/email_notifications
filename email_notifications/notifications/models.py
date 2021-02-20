from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date,datetime
# Create your models here.

class Ticket(models.Model):
    Ticket_ID = models.IntegerField(unique=True)
    Subject = models.CharField(max_length=256)
    Status = models.CharField(max_length=256)
    Source = models.CharField(max_length=256)
    Type = models.CharField(max_length=256)
    Agent = models.CharField(max_length=256)
    Group = models.CharField(max_length=256)
    Created_time = models.DateTimeField(null=False)
    Product = models.CharField(max_length=256)
    Follow_up_Date = models.CharField(max_length=256,null=True)
    Estimated_Delivery_Date = models.CharField(max_length=256,null=True)
    Full_name = models.CharField(max_length=256)
    Email = models.EmailField(max_length=256)
    Company_Name = models.CharField(max_length=256)
    def __str__(self):
        return self.Subject

class Confirmed_Ticket(models.Model):
    Ticket_ID = models.IntegerField(unique=True)
    Created_time = models.DateTimeField()
    updated_time = models.DateField(default=date.today())

    def __str__(self):
        return str(self.Ticket_ID)
