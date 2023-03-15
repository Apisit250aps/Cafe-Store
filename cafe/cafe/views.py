from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse
from .models import *

# Create your views here.


def homepage(request):
    if request.GET.get('search'):
        print(request.GET.get('search'))
    
    
    value = {
        "user":request.user,
        "menu":{
            "all":Menu.objects.all()
        }
    }
    
    for i in Categories.objects.all():
        
        cat = i.category
        if Menu.objects.filter(category=cat).count() != 0:
            value['menu'][cat] = Menu.objects.filter(category=cat)
        
        
    
    return render(request, 'cafe/home.html', value)


def search(request):
    if request.GET.get('search') != '':
        key = request.GET.get('search')
        results = Menu.objects.raw(f"SELECT * FROM `cafe_menu` WHERE menu LIKE '%{key}%' OR category LIKE '%{key}%'")
        # results = Menu.objects.filter(menu__contains=key, category__contains=key)
    else :
        return redirect('/')
        
    value = {
        "results":results,
        "more":Menu.objects.all(),
        "key":key
    }
    
    return render(request, 'cafe/result.html', value)


def detail(request):
    print(request.user.is_authenticated)
    
    value = {
        
        
    }
    key  = request.GET.get('id')
    value['detail'] = Menu.objects.filter(id=key)
    
    
    return render(request, 'cafe/detail.html', value)