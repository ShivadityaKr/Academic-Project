from django.urls import path
from . import views 
from .views import *
urlpatterns =[
    path('',views.home),
    path('sign',sign),
    path('login',login),
    path('logi',logi),
    path('forget',forget),
    path('Forgot',Forgot),
    path('change',change),
    path('chng',chng),
]
