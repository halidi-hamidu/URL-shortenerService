
from django.urls import path
from . import views


app_name= 'urlShortenApp'
urlpatterns = [
    path('', views.homePage, name ='homePage'),
]
