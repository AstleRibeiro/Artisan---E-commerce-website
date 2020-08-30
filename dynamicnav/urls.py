from . import views
from django.urls import path

app_name = 'dynamicnav'

urlpatterns = [
    path('', views.dyna, name='dyna'),
    path('acrylicpaintings/', views.acrylicpaintings, name='acrylicpaintings'),
    path('pastelpaintings/', views.pastelpaintings, name='pastelpaintings'),
    path('inkpaintings/', views.inkpaintings, name='inkpaintings'),

]
