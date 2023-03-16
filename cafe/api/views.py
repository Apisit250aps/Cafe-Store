from django.shortcuts import render
from django_filters import *

import pandas as pd 

from rest_framework.response import Response
from rest_framework.decorators import api_view

from cafe.models import *
from.serializers import MenuSerializer


@api_view(['GET',])
def getData(request):
    
    menu = Menu.objects.all()
    serializer = MenuSerializer(menu, many=True)
    
    return Response(serializer.data)


