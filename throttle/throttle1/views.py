from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Custom, Owner
from .serializers import CustomSerializer,CustomSerializer2 ,OwnerSerializer

from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
# from rest_framework.throttling import ScopedRateThrottle,UserRateThrottle,AnonRateThrottle

# from throttle1.throttling import JackRateThrottle

def fun(request):
    return HttpResponse("Hello") 

class CustomDetailAPI(APIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=[SessionAuthentication]
    def get(self, request, id=None, format=None):
        if id:
            customer = Custom.objects.get(id=id)
            serializer = CustomSerializer(customer)
            return Response(serializer.data)
        customer = Custom.objects.all()
        serializer = CustomSerializer(customer,many=True)
        return Response(serializer.data)

 


# class CustomDetailAPI1(viewsets.ModelViewSet):

#         queryset = Custom.objects.all()
#         serializer_class = CustomSerializer
#         permission_classes=[IsAuthenticatedOrReadOnly]
#         authentication_classes=[SessionAuthentication]
#         # throttle_classes=[AnonRateThrottle,UserRateThrottle]
#         throttle_classes=[AnonRateThrottle,JackRateThrottle]

#         throttle_classes=[ScopedRateThrottle]
#         throttle_scope=['viewsru']
class CustoAPI(APIView):
    def get_queryset(self):
        return super().get_queryset()
    

class CustomDetailAPI2(viewsets.ModelViewSet):
        queryset = Custom.objects.all()
        serializer_class = CustomSerializer2

class DetailAPI1(viewsets.ModelViewSet):
        queryset = Custom.objects.all()
        serializer_class = CustomSerializer

class DetailAPI2(viewsets.ModelViewSet):
        queryset = Owner.objects.all()
        serializer_class = OwnerSerializer