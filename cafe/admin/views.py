from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from cafe.models import *

import os
import random

# Create your views here.


def dashboard(request):
    value = {
        'title': "Dashboard"
    }
    return render(request, 'admin/dashboard.html', value)


def menu(request):

    value = {
        'title': 'Add menu',
        'category': Categories.objects.all()

    }
    return render(request, 'admin/menu.html', value)


def addMenu(request):

    var_menu = request.POST.get('menu', None)
    var_cat = request.POST.get('cat', None)
    var_desc = request.POST.get('description', None)
    var_price = request.POST.get('price', None)
    var_s_price = request.POST.get('s-price', None)
    var_m_price = request.POST.get('m-price', None)
    var_l_price = request.POST.get('l-price', None)

    picture = request.FILES['picture']
    print(picture)

    if os.path.exists(f'media/menu/{picture.name}'):
        sp = picture.name.split('.', 1)
        name = sp[0]
        ext = sp[1]

        picture.name = f'{name}_{random.randint(1000, 9999)}.{ext}'

    with open(f'media/menu/{picture.name}', 'wb+') as target:
        for chunk in picture.chunks():
            if target.write(chunk):
                Menu.objects.create(picture=picture, menu=var_menu, category=var_cat, description=var_desc,
                                    price=var_price, s_price=var_s_price, m_price=var_m_price, l_price=var_l_price).save()
                

                return render(request, 'admin/dashboard.html')
