from django.urls import path,include
from . import views

app_name= "home"

urlpatterns=[
    path('',views.home,name='home'),
    path('sales/',views.salesremainder,name='salesremainder'),
    path('upload/',views.upload,name='upload'),
    path('dashboard/',views.dashboard,name='dashboard'),

]
