from django.urls import path
from .views import *


urlpatterns = [
    path('', MAINPAGE, name = 'mainpage'), # Главная страница (мб новости, мб что-то ещё)
    path('alltickets', ALLTICKETSPAGE, name = 'allticketspage'), # Страница на которой будут находится все билеты всех рейсов
    path('tick/<int:ticketsid>/', TICKET, name = 'ticket'), # Подшаблонная страница для каждого определенного рейса
    path('about', ABOUT, name = 'about'),
    path('adminpanel', ADMINPANEL, name = 'adminpanel'),
    path('news/<slug:news_slug>/', SHOWNEWS, name = 'news'),
    path('category/<int:cat_id>/', SHOWCATEGORY, name = 'category'),
    path('addnews', ADDNEWS, name = 'addnews')
]