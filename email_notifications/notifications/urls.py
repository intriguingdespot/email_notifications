from django.urls import path,include
from . import views

app_name= "home"

urlpatterns=[
    path('',views.home,name='home'),
    path('braindesk-deliverables/',views.braindesk_confirm,name='braindesk_confirm'),
    path('universe-deliverables/',views.universe_confirm,name='universe_confirm'),
    path('sales/',views.salesremainder,name='salesremainder'),
    path('sales/braindesk',views.braindesk,name='braindesk'),
    path('sales/universe',views.universe,name='universe'),
    path('sales/others',views.others,name='others'),
    path('upload/',views.upload,name='upload'),
    #path('sales/status',views.status,name='status'),
]
