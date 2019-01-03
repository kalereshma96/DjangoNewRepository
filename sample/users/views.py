from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserLoginSerializer
from .forms import UseRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

def post(self, request, *args, **kwargs):
    data = request.data
    serializer = UserLoginSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        new_data = serializer.data
        return Response(new_data, status=HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
