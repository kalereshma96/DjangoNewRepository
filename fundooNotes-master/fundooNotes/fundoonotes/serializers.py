from django.contrib.auth.models import User
from rest_framework import serializers
from fundoonotes.models import Notes


class FundooNotesUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class FundooNotesSerializer(serializers.ModelSerializer):
    user = FundooNotesUserSerializer(read_only=True)

    class Meta:
        model = Notes
        fields = ("user", "name", "done", "date_created")
