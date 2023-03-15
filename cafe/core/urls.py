"""cafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers, serializers, viewsets

from django.conf import settings
from django.conf.urls.static import static

from manager import views as manage
from cafe import views as cafe

from api import views as api

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('manage/', manage.dashboard, name='dashboard'),
    path('manege/menu', manage.menu, name='menu'),
    path('manage/menu/add', manage.addMenu, name='add-menu'),
    path('manage/menu/del', manage.menuDelete, name='del'),
    path('manage/menu/edit', manage.menuEdit, name='edit'),
    path('', cafe.homepage, name='home'),
    path('result/', cafe.search, name='search'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
