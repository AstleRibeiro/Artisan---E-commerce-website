from . import views
from django.urls import path

app_name = 'add_to_cart'

urlpatterns = [
    path('add_to_cart/', views.cart, name='add_to_cart')
]