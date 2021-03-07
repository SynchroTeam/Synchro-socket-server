from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from .decorator import customIsAuthenticated
from .decoder import tokenDecoder
import subprocess

# Create your views here.

@api_view(['POST'])
@permission_classes([customIsAuthenticated])
def CreateChannel(request):

    # get token Payload
    token = request.headers['Authorization']
    tokenPayload = tokenDecoder(token)

    userId = tokenPayload['ID_CONSUMER']
    username = tokenPayload['USERNAME']


    return JsonResponse({
        'username': 'login to other service'
    },status = 200)