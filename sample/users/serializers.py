from django.db.models import Q
from django.forms import CharField, EmailField
from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
from django.db.models.serializers import  ModelSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only= True)
    email = EmailField(label='Email Address', allow_blank= True)

    class Meta:
            model = User
            fields = [
                'email',
                'password',
                'token'
            ]

            extra_kwargs = {"password":
                                {"write_only": True}}
def validate(self, data):
     user_obj = None
     email = data.get("email", None)
     password = data["password"]
     if not email:
      raise ValidationError('A username or email is required to login')
     user = User.objects.filter(
      Q(email=email)
                ).distinct()
     if user.exists() and user.count() == 1:
                user_obj = user.first()
     else:
       raise ValidationError("this email is not valid")

     if user_obj:
       if not user_obj.check_password(password):
           raise ValidationError("incorrect creadeintial try again")
     data["token"] = "SOME BLANK TOKEN"
     return data