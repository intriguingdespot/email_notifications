from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket
import pandas as pd
from datetime import date

import csv , io

from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

# Create your views here.
def login(request):
    return render(request,'notifications/login.html')

def dashboard(request):
    if request.method == "POST":
        today=str(date.today())
        tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today)
        tick_dict = {'Ticket':tickets}
        #send_mail(
        #'You have Deliverable Today !!!',
        #"Good Eve !!!",
        #settings.EMAIL_HOST_USER,
        #['kesavan.ramalingam@draup.com'],
        #fail_silently=False)
        #print("mail sent sucess fully")
        html_content = render_to_string("notifications/notification.html",context=tick_dict)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "You have a Deliverable !!",
        text_content,
        settings.EMAIL_HOST_USER,
        ['intriguing.despot@gmail.com'],
        cc=['kesavan.ramalingam@draup.com']
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
    return render(request,'notifications/dashboard.html')

def salesview(request):
    today=str(date.today())
    tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today)
    tick_dict = {'Ticket':tickets}
    return render(request,'notifications/sales.html',context=tick_dict)

def upload(request):
    if request.method == 'POST':
        tickets=Ticket.objects.all()
        tickets.delete()
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'Please use csv')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string,delimiter=","):
            created = Ticket.objects.update_or_create(
            Ticket_ID = column[0],
            Subject = column[1],
            Status = column[2],
            Source = column[3],
            Type = column[4],
            Agent = column[5],
            Group = column[6],
            Created_time = column[7],
            Product = column[8],
            Follow_up_Date = column[9],
            Estimated_Delivery_Date = column[10],
            Full_name = column[11],
            Email = column[12],
            Company_Name = column[13],
            )
        context = {}
        return render(request,'notifications/sales.html',context)
    return render(request,'notifications/upload.html')
