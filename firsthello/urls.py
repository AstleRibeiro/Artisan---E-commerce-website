from django.urls import path
from . import views

app_name='firsthello'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('aboutus/', views.about, name='aboutus'),
    path('auction/', views.auction, name='auction'),
    path('', views.index),



]
