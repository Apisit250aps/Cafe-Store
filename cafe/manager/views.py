from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from cafe.models import *

import os
import random

# Create your views here.



def menuEdit(request):
    
    var_id = request.POST.get('id')
    var_menu = request.POST.get('menu', None)
    var_cat = request.POST.get('cat', None)
    var_desc = request.POST.get('desc', None)
    var_price = request.POST.get('price', 0)
    var_s_price = request.POST.get('s-price', 0)
    var_m_price = request.POST.get('m-price', 0)
    var_l_price = request.POST.get('l-price', 0)
    
    df_picture = Menu.objects.get(id=var_id).picture

    var_picture = df_picture
    df = Menu.objects.get(id=var_id)
    update = Menu.objects.filter(id=var_id).update(menu=var_menu,
                                                   category=var_cat,
                                                   description=var_desc,
                                                   price=var_price,
                                                   s_price=var_s_price,
                                                   m_price=var_m_price,
                                                   l_price=var_l_price,
                                                   picture=var_picture
                                                   )

    try:
        update
    except:
        Menu.objects.filter(id=var_id).update(menu=df.menu,
                                              category=df.category,
                                              description=df.description,
                                              price=df.price,
                                              s_price=df.s_price,
                                              m_price=df.m_price,
                                              l_price=df.l_price,
                                              picture=df.picture
                                              )

    else:
        return redirect('menu')


def menuDelete(request):
    key = request.POST.get('id')

    for menu in Menu.objects.filter(id=key):
        os.remove(f"media/{menu.picture}")
        Menu.objects.get(id=key).delete()
        return redirect('menu')


def dashboard(request):
    value = {
        'title': "Dashboard"
    }
    return render(request, 'manager/dashboard.html', value)


def menu(request):
    print(request.user)

    value = {
        'title': 'Add menu',
        'category': Categories.objects.all(),
        'menu': Menu.objects.all()

    }
    return render(request, 'manager/menu.html', value)


def addMenu(request):

    var_menu = request.POST.get('menu', None)
    var_cat = request.POST.get('cat', None)
    var_desc = request.POST.get('description', None)
    var_price = request.POST.get('price', 0)
    var_s_price = request.POST.get('s-price', 0)
    var_m_price = request.POST.get('m-price', 0)
    var_l_price = request.POST.get('l-price', 0)

    picture = request.FILES['picture']
    print(picture)
    
    

    if os.path.exists(f'media/menu/{picture.name}'):
        sp = picture.name.split('.', 1)
        name = sp[0]
        ext = sp[1]

        picture.name = f'{name}_{random.randint(1000, 9999)}.{ext}'

    try:
        Menu.objects.create(picture=picture,
                            menu=var_menu,
                            category=var_cat,
                            description=var_desc,
                            price=var_price,
                            s_price=var_s_price,
                            m_price=var_m_price,
                            l_price=var_l_price).save()

    except:
        os.remove(f"media/{menu.picture}")

    else:

        return redirect('menu')


def uploadFiles(file):
    if os.path.exists(f'media/menu/{file.name}'):
        sp = file.name.split('.', 1)
        name = sp[0]
        ext = sp[1]

        file.name = f'{name}_{random.randint(1000, 9999)}.{ext}'

    with open(f'media/menu/{file.name}', 'wb+') as target:
        for chunk in file.chunks():
            print(chunk)
            if target.write(chunk):
                return True
            else:
                return False
