from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views as cafe

urlpatterns = [
    path('category/', cafe.getCategory, name='category'),
    path('provinces/', cafe.provinceThailand, name='prov'),
    path('district/', cafe.districtThailand, name='dist'),
    path('tambon/', cafe.tambonThailand, name='tamb'),
]
