from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
# Create your views here.


def MAINPAGE(request):
    news = News.objects.all()
    cats = Category.objects.all()
    return render(request, 'aviato/index.html', {'title': 'Билеты и авиановости - Aviato',
                                                 'news': news,
                                                 'cats': cats,
                                                     'cat_selected': 0})

def ALLTICKETSPAGE(request):
    posts = User.objects.all()
    return render(request, 'aviato/all_tickets_page.html', {'title': 'Купить билеты - Aviato', 'posts': posts})

def TICKET(request, ticketsid):
    return HttpResponse(f"TICKET PAGE <p>{ticketsid}</p>")

def ABOUT(requset):
    return render(requset, 'aviato/about.html', {'title': 'Подробнее'})
def ADMINPANEL(request):
    news = News.objects.all()
    users = User.objects.all()
    cats = Category.objects.all()
    return render(request, 'aviato/all_users.html', {'title': 'Все пользователи',
                                                     'users': users,
                                                     'news': news,
                                                     'cats': cats,
                                                     'cat_selected': 0})

def SHOWNEWS(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)

    context = {
        'news': news,
        'title': news.title,
        'photo': news.photo,
        'content': news.content,
        'cat': news.cat,
    }

    return render(request, 'aviato/newspage.html', context=context)

def SHOWCATEGORY(request, cat_id):
    return HttpResponse(f"{cat_id}")



def ADDNEWS(request):
    return render(request, 'aviato/addnews.html', {'title': 'Добавление новости'})



#!!! Ошибки
def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')