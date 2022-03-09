from django.urls import path
from .views import *

urlpatterns = [
    path('', MAINPAGE), # Главная страница (мб новости, мб что-то ещё)
    path('alltickets', ALLTICKETSPAGE), # Страница на которой будут находится все билеты всех рейсов
    path('tick/<int:ticketsid>/', TICKET), # Подшаблонная страница для каждого определенного рейса
]