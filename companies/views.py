from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.mixins import UpdateModelMixin
from rest_framework.decorators import api_view

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = Users.objects.all()
        username = self.request.query_params.get('name', None)
        if username is not None:
            queryset = queryset.filter(name__icontains=username)
        return queryset

class UsersCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                query = Users.objects.get(name=serializer.validated_data.get('name',None))
                serializer = UserSerializer(query, data=serializer.validated_data)
            except Users.DoesNotExist:
                serializer = UserSerializer( data=serializer.validated_data)
                
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

