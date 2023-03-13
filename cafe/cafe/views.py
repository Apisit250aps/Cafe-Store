from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def homepage(request):
    return render(request, 'cafe/home.html')