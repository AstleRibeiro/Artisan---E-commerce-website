from django.conf.urls import url

from . import views
from django.urls import path

app_name = 'add_to_cart'

urlpatterns = [
    path('add_to_cart/', views.cart, name='add_to_cart'),
    path('yourorders/', views.yourorders, name='yourorders'),
    path('handlerequest/', views.handlerequest, name='HandleRequest'),


]