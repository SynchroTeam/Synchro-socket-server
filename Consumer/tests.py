from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.test import Client 
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from decouple import config


class CreateCunsumer(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testname', email='test@test.com', password='top_secret'
        )

    def test_details(self):

        # login and get token   
        user = User.objects.get(username='testname')

        self.assertEqual(user.username, 'testname')