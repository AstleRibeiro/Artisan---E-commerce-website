from . import views
from django.urls import path

app_name = 'photographs'

urlpatterns = [
    path('', views.Architectural, name='Architectural'),
    path('aerial/', views.Aerial, name='Aerial'),
    path('fineart/', views.Fineart, name='Fineart'),
    path('fashion/', views.Fashion, name='Fashion'),
    path('sports/', views.Sports, name='Sports'),
    path('portraits/', views.Portraits, name='Portraits'),
    path('aerial_description/<int:id>', views.aerial_description, name='aerial_description'),
    path('architectural_description/<int:id>', views.aerial_description, name='architectural_description'),

]
