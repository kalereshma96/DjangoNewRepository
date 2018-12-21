from django.shortcuts import render
from  django.http import HttpResponse
from django.shortcuts import get_object_or_404
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import login
from .serializers import loginSerializer


# Create your views here.
class userList(APIView):

    def get(self, request):
        login1 = login.objects.all() #store all object of employee in employees1
        serializer =loginSerializer(login1, many = True)
        return Response(serializer.data)

    def post(self):
        pass