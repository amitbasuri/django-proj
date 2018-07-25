from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from .models import Users
from .serializers import UserSerializer
from rest_framework import generics

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = Users.objects.all()
        username = self.request.query_params.get('name', None)
        if username is not None:
            queryset = queryset.filter(name__icontains=username)
        return queryset

class UsersCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()