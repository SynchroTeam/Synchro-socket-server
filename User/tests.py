from django.test import  TestCase
from django.test import Client 
import jwt
from decouple import config

class CreateUser(TestCase):

    def test_details(self):

        AUTHORIZATION = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE1MTI4NTQ2LCJqdGkiOiJiNmI5NGFiMzg0MGQ0ZjMyOWVkZjg1YWZlMmE5NGQzZSIsInVzZXJfaWQiOiIxY2ZlMDNjYy0zODY3LTQ0MzgtODZlZi03MDAyNWQxNjc2NDEiLCJQRVJNSVNJT05TIjpbXSwiVVNFUk5BTUUiOiJqYWNvYiIsIklEX0NPTlNVTUVSIjoiMWNmZTAzY2MtMzg2Ny00NDM4LTg2ZWYtNzAwMjVkMTY3NjQxIiwiRVhQIjoxNjE1MTI4NTQ2fQ.eihN8l5ZddMRPH4hu5HxvUORbMK7OEHM7HxC8prTlvs'
        ID_CHANNEL = "89edfa70-7f4c-11eb-912d-af4bf29ca96d"
        # BLUE_PRINT =  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e30.6_IVKSoFcLzSmvH82p1MpE2k0iIQIp9H1TErw7i4vaE"

        self.client = Client(HTTP_AUTHORIZATION=  AUTHORIZATION)

        respose = self.client.post("/api/v0/user/create/",{
            'ID_CHANNEL' : ID_CHANNEL,
            'ID_USER': '1'
        })
        
        print(respose.json())
        self.assertTrue(respose.json()['JWT_USER'])
        self.assertEqual(respose.status_code, 200)
