from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.test import Client 
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from decouple import config
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
import time
import datetime
import uuid

class CreateChannel(TestCase):

    def test_details(self):

        dt = datetime.datetime.strptime('2022-02-09', '%Y-%m-%d')

        JTW = {
            'EXP': time.mktime(dt.timetuple()),
            'ID_CONSUMER': str(uuid.uuid1()),
            'PERMISIONS': [],
            'USERNAME': 'James'
        }

        encoded = jwt.encode(JTW, config('SECRET_KEY'), algorithm="HS256")

        self.client = Client(HTTP_AUTHORIZATION=  encoded)

        respose = self.client.post("/api/v0/channel/create/",{})
        
        self.assertTrue(respose.json()['ID_CHANNEL'])
        self.assertTrue(respose.json()['BLUE_PRINT'])
        self.assertEqual(respose.status_code, 200)
