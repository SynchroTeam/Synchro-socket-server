
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
import jwt
from .decoder import tokenDecoder

class customIsAuthenticated(BasePermission):
    message = 'Token expired'

    def has_permission(self,request,*args,**kwargs):

        accessToken = request.headers['Authorization']

        try:
            decodeJTW = tokenDecoder(accessToken)
            return True
        except:
            self.message = 'Token is expired' 
            return False