"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from TiF import views

router=routers.DefaultRouter()
router.register(r'Text',views.TextModeViewSet)
router.register(r'get-category',views.FoundationTree)
router.register(r'category-tree',views.CategoryTree)
router.register(r'createText',views.CreateText)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('djoser.urls')),
    path('registration/', views.RegistrUserView.as_view(), name='registr'),
    path('auth/',include('djoser.urls.authtoken')),
    path('auth/',include('djoser.urls.jwt')),
]+router.urls
