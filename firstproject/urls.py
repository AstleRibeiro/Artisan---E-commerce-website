"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firsthello.urls')),
    path('dyna/', include('dynamicnav.urls', namespace='dyna')),
    path('madhubani/', include('madhubani.urls', namespace='madhubani')),
    path('corporate/', include('forposters.urls')),
    path('architectural/', include('photographs.urls')),
    path('deepset/', include('frames.urls')),
    path('contactus/', include('contactus.urls')),
    path('add_to_cart/', include('add_to_cart.urls', namespace='add_to_cart')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('thanks/', views.Thankspage.as_view(), name='thanks'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
