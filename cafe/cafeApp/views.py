from django.shortcuts import render

# Create your views here.

import json
from django.shortcuts import render, redirect, get_object_or_404
import os
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles import finders
from django.contrib.auth import authenticate, login, logout
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

    # get thai province file
    # result = finders.find('data/thai_province.json')

    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)
    # return Response({'status': True, 'message': msg, 'data': data}, status=http_status)
