from django.shortcuts import render

# Create your views here.

def homepage(req):
    
    return render(req, 'index.html')


def login(req):
    
    return render(req, 'gate/login.html')