
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from decouple import config
from .decorator import customIsAuthenticated
from .decoder import tokenDecoder
import hashlib 
import uuid
import jwt

# Create your views here.

@api_view(['POST'])
@permission_classes([customIsAuthenticated])
def CreateChannel(request):

    # get token Payload
    token = request.headers['Authorization']
    tokenPayload = tokenDecoder(token)

    ID_CONSUMER = tokenPayload['ID_CONSUMER']
    ID_CHANNEL = str(uuid.uuid1())

    to_hash = config('SECRET_KEY') + ID_CONSUMER +  ID_CHANNEL

    hash_class = hashlib.sha1((to_hash).encode()) 
    
    # Varies accordingly ID_CONSUMER ID_CHANNEL
    channel_key = hash_class.hexdigest()

    CHANNEL_CONFIG = {

    }

    BLUE_PRINT = jwt.encode(CHANNEL_CONFIG, channel_key, algorithm="HS256")

    return Response({
        'ID_CHANNEL': ID_CHANNEL,
        'BLUE_PRINT': BLUE_PRINT
    }, status = 200)