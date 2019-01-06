import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Notes
from .serializers import FundooNotesSerializer


class FundooNotesListCreateAPIViewTestCase(APITestCase):
    url = reverse("fundoonotes:list")

    def setUp(self):
        self.username = "xyz"
        self.email = "kalereshma96@gmail.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_fundoonotes(self):
        response = self.client.post(self.url, {"name": "Clean the room!"})
        self.assertEqual(201, response.status_code)

    def test_user_fundoonotes(self):
        """
        Test to verify user fundoonotes list
        """
        Notes.objects.create(user=self.user, name="Clean the car!")
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Notes.objects.count())


class FundooNotesDetailAPIViewTestCase(APITestCase):

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.notes = Notes.objects.create(user=self.user, name="Call Mom!")
        self.url = reverse("fundoonotes:detail", kwargs={"pk": self.notes.pk})
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_fundoonotes_object_bundle(self):
        """
        Test to verify notes object bundle
        """
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        fundoonotes_serializer_data = FundooNotesSerializer(instance=self.notes).data
        response_data = json.loads(response.content)
        self.assertEqual(fundoonotes_serializer_data, response_data)

    def test_fundoonotes_object_update_authorization(self):
        """
            Test to verify that put call with different user token
        """
        new_user = User.objects.create_user("newuser", "new@user.com", "newpass")
        new_token = Token.objects.create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)

        # HTTP PUT
        response = self.client.put(self.url, {"name", "Hacked by new user"})
        self.assertEqual(403, response.status_code)

        # HTTP PATCH
        response = self.client.patch(self.url, {"name", "Hacked by new user"})
        self.assertEqual(403, response.status_code)

    def test_fundoonotes_object_update(self):
        response = self.client.put(self.url, {"name": "Call Dad!"})
        response_data = json.loads(response.content)
        notes = Notes.objects.get(id=self.notes.id)
        self.assertEqual(response_data.get("name"), notes.name)

    def test_fundoonotes_object_partial_update(self):
        response = self.client.patch(self.url, {"done": True})
        response_data = json.loads(response.content)
        notes = Notes.objects.get(id=self.notes.id)
        self.assertEqual(response_data.get("done"), notes.done)

    def test_fundoonotes_object_delete_authorization(self):
        """
            Test to verify that put call with different user token
        """
        new_user = User.objects.create_user("newuser", "new@user.com", "newpass")
        new_token = Token.objects.create(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)
        response = self.client.delete(self.url)
        self.assertEqual(403, response.status_code)

    def test_fundoonotes_object_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)
