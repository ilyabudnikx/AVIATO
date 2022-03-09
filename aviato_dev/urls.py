from django.urls import path
from .views import *

urlpatterns = [
    path('', MAINPAGE),
    path('tickets', ALLTICKETSPAGE),
    path('tick/<int:ticketsid>/', TICKET),
]