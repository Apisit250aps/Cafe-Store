from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views as cafe

urlpatterns = [
    path('api/category/', cafe.getCategory, name='category'),
    path('api/provinces/', cafe.provinceThailand, name='prov'),
    path('api/district/', cafe.districtThailand, name='dist'),
    path('api/tambon/', cafe.tambonThailand, name='tamb'),
]
