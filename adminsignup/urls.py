from django.contrib import admin
from django.urls import path,include 
from adminsignup import views
urlpatterns = [
    path('', views.login,name="login"),
    path('asignup', views.adminsignup,name="asignup"),
    path('alogin', views.adminlogin,name="alogin"),
    path('dashboard', views.admindashboard,name="dashboard"),
    path('addevent', views.addevent,name="addevent"),

    
]
