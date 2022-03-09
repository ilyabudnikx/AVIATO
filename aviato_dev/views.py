from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
def MAINPAGE(request):
    return HttpResponse("<H1>MAIN PAGE AVIATO</H1>")

def ALLTICKETSPAGE(request):
    return HttpResponse("TICKETS PAGE")

def TICKET(request, ticketsid):
    return HttpResponse(f"TICKET PAGE <p>{ticketsid}</p>")







#!!! Ошибки
def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')