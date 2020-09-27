from . import views
from django.urls import path

app_name = 'forposters'

urlpatterns = [
    path('', views.corporatePosters, name='corporatePosters'),
    path('campaign/', views.campaignPosters, name='campaignPosters'),
    path('political/', views.politicalPosters, name='politicalPosters'),
    path('show/', views.showPosters, name='showPosters'),
    path('show_description/<int:id>/', views.show_description, name='showposter'),

]
