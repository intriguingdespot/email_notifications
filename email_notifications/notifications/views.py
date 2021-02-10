from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def login(request):
    return render(request,'notifications/login.html')

def dashboard(request):
    if request.method == "POST":
        send_mail('Hello !!','hi',settings.EMAIL_HOST_USER,['intriguing.despot@gmail.com'],fail_silently=False)
    return render(request,'notifications/dashboard.html')
