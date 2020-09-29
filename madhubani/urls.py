from . import views
from django.urls import path

app_name = 'madhubani'

urlpatterns = [
    path('', views.MadhubaniHome, name='madhubani'),
    path('madhubani_description/<int:id>', views.Madhubani_description, name='madhubani_description'),

]
