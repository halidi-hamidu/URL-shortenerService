
from django.urls import path
from . import views


app_name = 'authApp'

urlpatterns = [
    path('', views.loginPage, name ='loginPage'),
    path('login/', views.loginPage, name ='loginPage'),
    path('logout/', views.logoutPage, name ='logout'),
    path('register/', views.registerPage, name ='registerPage'),
]
