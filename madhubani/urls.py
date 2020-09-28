from . import views
from django.urls import path

app_name = 'madhubani'

urlpatterns = [
    path('', views.MadhubaniHome, name='madhubani'),

]