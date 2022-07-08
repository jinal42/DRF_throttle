"""throttle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from throttle1 import views

from rest_framework.routers import DefaultRouter
from throttle1 import  views as v

router = DefaultRouter()

# router.register('v',v.CustomDetailAPI1,basename='v')   
router.register('h',v.CustomDetailAPI2,basename='customer')   

router.register('details-1',v.DetailAPI1,basename='detail-1')   
router.register('details-2',v.DetailAPI2,basename='detail-2')  
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),


    path('fun/', views.fun),
    path('cust/', views.CustomDetailAPI.as_view()),
    path('cust/<int:id>/', views.CustomDetailAPI.as_view()),
    # path('get/', views.CustomDetailAPI1.as_view()),
    path('auth/',include('rest_framework.urls')),
#   path('auth/', include('rest_framework.urls', namespace = 'rest_framework'))

]


