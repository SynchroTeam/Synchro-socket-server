from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from django.test import Client 
from django.contrib.auth import authenticate, get_user_model
Consumer = get_user_model()

class SignupTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = Consumer.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_secret'
        )

    def test_details(self):

        # login and get token
        respose = self.client.post("/api/v0/consumer/login/", data={
            'username': 'jacob',
            'password': 'top_secret'
        })
        
        
        self.assertTrue(respose.json()['access'])
        self.assertEqual(respose.status_code, 201)