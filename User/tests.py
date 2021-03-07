from django.test import  TestCase
from django.test import Client 
from decouple import config
import jwt
import time
import datetime
import uuid

class CreateUser(TestCase):

    def test_details(self):

        dt = datetime.datetime.strptime('2022-02-09', '%Y-%m-%d')

        JTW_CONSUMER = {
            'EXP': time.mktime(dt.timetuple()),
            'exp':  time.mktime(dt.timetuple()),
            'ID_CONSUMER': str(uuid.uuid1()),
            'PERMISIONS': [],
            'USERNAME': 'James'
        }

        AUTHORIZATION = jwt.encode(JTW_CONSUMER, config('SECRET_KEY'), algorithm="HS256")

        ID_CHANNEL = "89edfa70-7f4c-11eb-912d-af4bf29ca96d"
        # BLUE_PRINT =  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e30.6_IVKSoFcLzSmvH82p1MpE2k0iIQIp9H1TErw7i4vaE"

        self.client = Client(HTTP_AUTHORIZATION=  AUTHORIZATION)

        respose = self.client.post("/api/v0/user/create/",{
            'ID_CHANNEL' : ID_CHANNEL,
            'ID_USER': '1'
        })

        self.assertTrue(respose.json()['JWT_USER'])
        self.assertEqual(respose.status_code, 200)