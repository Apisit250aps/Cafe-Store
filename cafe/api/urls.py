from django.urls import path
from . import views as api


urlpatterns = [
    path('api', api.getData)
]




