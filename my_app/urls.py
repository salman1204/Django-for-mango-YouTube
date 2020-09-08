from django.contrib import admin
from django.urls import path 
from my_app import views

app_name = "my_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('form/', views.form, name="form"),
    
]
