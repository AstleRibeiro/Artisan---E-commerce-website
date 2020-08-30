from django.urls import path
from . import views

app_name='firsthello'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('', views.index),


]
