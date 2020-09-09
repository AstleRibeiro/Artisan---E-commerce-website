from . import views
from django.urls import path

app_name = 'frames'

urlpatterns = [
    path('', views.DeepSet1, name='DeepSet1'),
    path('floating/', views.Floating1, name='Floating1'),
    path('gallery/', views.Gallery1, name='Gallery1'),
    path('modern/', views.Modern1, name='Modern1'),
    path('tabletop/', views.TableTop1, name='TableTop1'),


]
