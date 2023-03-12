from django.shortcuts import render
from cafe.models import *

# Create your views here.

def dashboard(request):
    value = {
        'title':"Dashboard"
    }
    return render(request , 'admin/dashboard.html', value)

def menu(request):
    
    value = {
        'title':'Add menu',
        'category':Categories.objects.all()
        
    }    
    return render(request , 'admin/menu.html', value)