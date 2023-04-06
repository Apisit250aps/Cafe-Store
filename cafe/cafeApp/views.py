import json
import pytz
from PIL import Image
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles import finders
from django.contrib.auth import authenticate, login
from django.db.models import Q


from .models import *
from .serializers import *

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.

@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def getCategory(request):
    data = {}
    msg = 'already get thai province'
    http_status = HTTP_200_OK

    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def provinceThailand(request):
    data = {}
    result = finders.find('data/thai_province.json')
    with open(result, encoding="utf8") as f:
        province = json.load(f)
    
    data = province.keys()
    print(type(province))
    return Response(data)

@csrf_exempt
@api_view(["POST" ])
@permission_classes((AllowAny,))
def districtThailand(request):
    data = {}
    result = finders.find('data/thai_province.json')
    with open(result, encoding="utf8") as f:
        province = json.load(f)
   
    provinceSelect = request.data['province']
    print(provinceSelect)
    
    data = province[provinceSelect].keys()
   
    return Response({"status":True, "data":data})

@csrf_exempt
@api_view(["POST" ])
@permission_classes((AllowAny,))
def tambonThailand(request):
    data = {}
    result = finders.find('data/thai_province.json')
    with open(result, encoding="utf8") as f:
        province = json.load(f)
    provinceSelect = request.data['province']
    districtSelect = request.data['district']
    print(districtSelect)
    
    data = province[provinceSelect][districtSelect]
   
    return Response({"status":True, "data":data})