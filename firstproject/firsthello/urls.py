from django.urls import path
from . import views

app_name='firsthello'

urlpatterns = [
    path('', views.index),
    path('okay/', views.index1),

]
