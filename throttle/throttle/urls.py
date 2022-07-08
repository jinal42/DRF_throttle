from django.contrib import admin
from django.urls import path,include

from throttle1 import views

from rest_framework.routers import DefaultRouter
from throttle1 import  views as v
from Random_Number import views as random_view

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

    path('ran/',random_view.random_number),


]


