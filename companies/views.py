from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from .models import Users
from .serializers import UserSerializer


class UserList(APIView):

    def get(self,request):
        users = Users.objects.all()
        serializer = UserSerializer(users,many=True)
        return JsonResponse(serializer.data, safe=False)
