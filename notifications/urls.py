from django.urls import path,include
from . import views

app_name= "home"

urlpatterns=[
    path('',views.home,name='home'),
    path('today/braindesk-deliverables/',views.today_braindesk_confirm,name='today_braindesk_confirm'),
    path('today/universe-deliverables/',views.today_universe_confirm,name='today_universe_confirm'),
    path('tomorrow/braindesk-deliverables/',views.tomorrow_braindesk_confirm,name='tomorrow_braindesk_confirm'),
    path('tomorrow/universe-deliverables/',views.tomorrow_universe_confirm,name='tomorrow_universe_confirm'),
    path('sales/today-deliverables',views.todaydeliverables,name='todaydeliverables'),
    path('sales/tomorrow-deliverables',views.tomorrowdeliverables,name='tomorrowdeliverables'),
    path('sales/today-deliverables/braindesk',views.today_braindesk,name='today_braindesk'),
    path('sales/today-deliverables/universe',views.today_universe,name='today_universe'),
    path('sales/today-deliverables/others',views.today_others,name='today_others'),
    path('sales/tomorrow-deliverables/braindesk',views.tomorrow_braindesk,name='tomorrow_braindesk'),
    path('sales/tomorrow-deliverables/universe',views.tomorrow_universe,name='tomorrow_universe'),
    path('sales/tomorrow-deliverables/others',views.tomorrow_others,name='tomorrow_others'),
    path('upload/',views.upload,name='upload'),
    path('sales/today-status',views.ticket_status_today,name='ticket_status_today'),
]
