from django.urls import path,include
from . import views

app_name= "home"

urlpatterns=[
    path('',views.home,name='home'),
    path('sales/',views.salesremainder,name='salesremainder'),
    path('sales/braindesk',views.braindesk,name='braindesk'),
    path('sales/universe',views.universe,name='universe'),
    path('sales/others',views.others,name='others'),
    path('upload/',views.upload,name='upload'),
]
