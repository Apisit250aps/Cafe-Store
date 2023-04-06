from django.shortcuts import render

# Create your views here.

def homepage(request):
    
    return render(request, 'index.html')


def login(request):
    
    return render(request, 'gate/login.html')

def register(request):
    
    return render(request, 'gate/register.html')