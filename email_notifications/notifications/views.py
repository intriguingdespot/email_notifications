from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import operator
from django.db.models import Q
from functools import reduce
from django.urls import reverse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import Ticket,Confirmed_Ticket
from datetime import date,datetime
from django.utils import timezone


import csv , io

from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('home')
            else:
                return HttpResponse("user not active contact admin")
        else:
            return HttpResponse("Invalid, If you don't have the access or forgotted your credentials please reach us on customersupport_nemili@draup.com")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('home')
        else:
            return render(request,'notifications/login.html',{})
@login_required(login_url = 'login_user')
def home(request):
    return render(request,'notifications/landingpage.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_user'))

def thankyou(request):
    return render(request,'notifications/thankyou.html')

@login_required(login_url = 'login_user')
def salesremainder(request):
    today=str(date.today())
    tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today)
    tick_dict = {'Ticket':tickets}
    return render(request,'notifications/today_deliverables.html',context=tick_dict)


@login_required(login_url = 'login_user')
def braindesk(request):
    if request.method == "POST":
        today=str(date.today())
        tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today,Type__icontains="Braindesk Request")
        tick_dict = {'Ticket':tickets,'name':"Braindesk Team,","url":"braindesk-deliverables"}
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
        #cc=['kesavan.ramalingam@draup.com']
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        return salesremainder(request)
    else:
        today=str(date.today())
        tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today,Type__icontains="Braindesk Request")
        tick_dict = {'Ticket':tickets}
        return render(request,'notifications/braindesk_deliverables.html',context=tick_dict)

@login_required(login_url = 'login_user')
def universe(request):
    if request.method == "POST":
        today=str(date.today())
        tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today,Type__icontains = 'Universe Account Addition Request')
        tick_dict = {'Ticket':tickets,'name':"Universe Team,","url":"universe-deliverables"}
        html_content = render_to_string("notifications/notification.html",context=tick_dict)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "You have a Deliverable !!",
        text_content,
        settings.EMAIL_HOST_USER,
        ['intriguing.despot@gmail.com'],
        #cc=['kesavan.ramalingam@draup.com']
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        return salesremainder(request)
    else:
        today=str(date.today())
        tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today,Type__icontains = 'Universe Account Addition Request')
        tick_dict = {'Ticket':tickets}
        return render(request,'notifications/universe_deliverables.html',context=tick_dict)

@login_required(login_url = 'login_user')
def others(request):
    if request.method == "POST":
        today=str(date.today())
        tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today).exclude(Type__icontains = 'Universe Account Addition Request').exclude(Type__icontains="Braindesk Request")
        tick_dict = {'Ticket':tickets,'name':"Team,"}
        html_content = render_to_string("notifications/notification.html",context=tick_dict)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
        "You have a Deliverable !!",
        text_content,
        settings.EMAIL_HOST_USER,
        ['intriguing.despot@gmail.com'],
        #cc=['kesavan.ramalingam@draup.com']
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        return salesremainder(request)
    else:
        today=str(date.today())
        tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today).exclude(Type__icontains = 'Universe Account Addition Request').exclude(Type__icontains="Braindesk Request")
        tick_dict = {'Ticket':tickets}
        return render(request,'notifications/others_deliverables.html',context=tick_dict)

def braindesk_confirm(request):
    if request.method == "POST":
        some_var = request.POST.getlist('Ticket_ID')
        for i in some_var:
            Confirmed_Ticket.objects.update_or_create(Ticket_ID=i,Created_time=timezone.now())
        return thankyou(request)
    else:
        today=str(date.today())
        tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today,Type__icontains="Braindesk Request")
        tick_dict = {'Ticket':tickets}
        return render(request,'notifications/braindesk_confirm.html',context=tick_dict)

def universe_confirm(request):
    if request.method == "POST":
        some_var = request.POST.getlist('Ticket_ID')
        for i in some_var:
            Confirmed_Ticket.objects.update_or_create(Ticket_ID=i,Created_time=timezone.now())
        return thankyou(request)
    else:
        today=str(date.today())
        tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today,Type__icontains = 'Universe Account Addition Request')
        tick_dict = {'Ticket':tickets}
        return render(request,'notifications/universe_confirm.html',context=tick_dict)

def status(request):
    #d = datetime.now()
    #print(d)
    #print(d.date())
    Confirmed_Tickets = Confirmed_Ticket.objects.all()
    tick_dict = {'Ticket':Confirmed_Tickets}
    return render(request,'notifications/status.html',context=tick_dict)

@login_required(login_url = 'login_user')
def upload(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'Please use csv')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        tickets=Ticket.objects.all()
        tickets.delete()
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
        return home(request)
    return render(request,'notifications/upload.html')
