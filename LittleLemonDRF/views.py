from django.shortcuts import render
from .models import Rating
from rest_framework import generics
from .serializers import RatingSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission, IsAuthenticated

# Create your views here.
class RatingsView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    def get_permissions(self):
        if(self.request.method=='GET'):
            return []  
        return [IsAuthenticated()]
