from django.shortcuts import render
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import permissions
from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q

from .models import Register
from .serializer import Register_serializer
from .models import Message
from .serializer import Message_serializer

    
class Register_view(generics.ListCreateAPIView):
    serializer_class=Register_serializer
    permission_classes=[AllowAny]
    def get_queryset(self):
        login_user=self.request.user

        if not login_user.is_authenticated:
            return Register.objects.none()

        if login_user.Role=='admin':
            return Register.objects.all()
        else:
            return Register.objects.filter(id=login_user.id)
    
class Register_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Register.objects.all()
    serializer_class=Register_serializer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticated]


class MessagelistView(ListCreateAPIView):
    serializer_class=Message_serializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)  

class Chatlistview(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        user=request.user
        reciever_id=request.GET.get('reciever')
        messages=Message.objects.filter(
            Q(sender=user,reciever_id=reciever_id) | Q(sender_id=reciever_id,reciever=user)
        ).order_by('created_at')
        serializer=Message_serializer(messages, many=True)
        return Response(serializer.data)
# Create your views here.
