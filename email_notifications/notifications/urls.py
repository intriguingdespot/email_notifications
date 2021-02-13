from django.urls import path,include
from . import views

app_name= "home"

urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('sales/',views.salesview,name='salesview'),
    path('upload/',views.upload,name='upload'),

]
