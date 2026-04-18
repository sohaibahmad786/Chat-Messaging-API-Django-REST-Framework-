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

from .models import Register
from .serializer import Register_serializer
from .models import Search_data
from .serializer import Search_serializer
from .models import Students
from .serializer import Student_serializer
from .models import Task
from .serializer import Task_serializer

    
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

class Search_view(generics.ListCreateAPIView):
    queryset=Search_data.objects.all()
    serializer_class=Search_serializer
    filter_backends=[filters.SearchFilter]
    search_fields=['Name','About']
class Studentlist(generics.ListCreateAPIView):
    queryset=Students.objects.all()
    serializer_class=Student_serializer
class Studentdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Students.objects.all()
    serializer_class=Student_serializer

class Task_listview(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=Task_serializer
class Task_detailview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=Task_serializer
# Create your views here.
