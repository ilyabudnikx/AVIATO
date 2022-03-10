from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
menu = ["Главная","Подробнее", "Бронирование", "Управление", "Справка"]
def MAINPAGE(request):
    return render(request, 'aviato/index.html', {'title': 'Билеты и авиановости - Aviato'})

def ALLTICKETSPAGE(request):
    posts = User.objects.all()
    return render(request, 'aviato/all_tickets_page.html', {'title': 'Купить билеты - Aviato', 'posts': posts})

def TICKET(request, ticketsid):
    return HttpResponse(f"TICKET PAGE <p>{ticketsid}</p>")

def ABOUT(requset):
    return render(requset, 'aviato/about.html', {'title': 'Подробнее'})

def ADMINPANEL(request):
    users = User.objects.all()
    return render(request, 'aviato/all_users.html', {'title': 'Все пользователи', 'users': users})




#!!! Ошибки
def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')