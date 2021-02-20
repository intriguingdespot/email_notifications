from __future__ import absolute_import,unicode_literals

from celery import shared_task
import time

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

from django.db import IntegrityError


import csv , io

from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

@shared_task
def add(x, y):
    time.sleep(10)
    return x + y

@shared_task
def send_email(email):
    lis=['Braindesk Report Refresh Request','Braindesk Request']
    today=str(date.today())
    tickets = Ticket.objects.filter(Estimated_Delivery_Date__icontains=today,Type__in=lis)
    tick_dict = {'Ticket':tickets,'name':"Braindesk Team","url":"braindesk-deliverables"}
    html_content = render_to_string("notifications/notification1.html",context=tick_dict)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
    "You have a Braindesk Deliverable !!",
    text_content,
    settings.EMAIL_HOST_USER,
    ['intriguing.despot@gmail.com'],
    #cc=['kesavan.ramalingam@draup.com']
    )
    email.attach_alternative(html_content,"text/html")
    email.send()
    print(f' A sample message {email}')
