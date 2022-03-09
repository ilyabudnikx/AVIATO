from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def MAINPAGE(request):
    return HttpResponse("<H1>MAIN PAGE AVIATO</H1>")

def ALLTICKETSPAGE(request):
    return HttpResponse("TICKETS PAGE")

def TICKET(request, ticketsid):
    return HttpResponse(f"TICKET PAGE <p>{ticketsid}</p>")