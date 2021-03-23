from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
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
def create_user(request):

    # get token Payload
    token = request.headers['Authorization']
    tokenPayload = tokenDecoder(token)


    ID_CONSUMER = tokenPayload['ID_CONSUMER']
    ID_CHANNEL = request.POST.get("ID_CHANNEL")
    ID_USER = request.POST.get("ID_USER")

    jwt_payload = {
        'ID_CHANNEL': ID_CHANNEL,
        'ID_USER': ID_USER,
        'ID_CONSUMER': ID_CONSUMER,
        'ID_CONNECTION': str(uuid.uuid1())
    }

    # Hash combination
    to_hash = config('SECRET_KEY') +  ID_CHANNEL
    hash_class = hashlib.sha1((to_hash).encode()) 

    # Varies accordingly ID_CONSUMER ID_CHANNEL
    user_key = hash_class.hexdigest()


    JWT_USER = jwt.encode(jwt_payload, user_key, algorithm="HS256")

    return Response({
        'JWT_USER': JWT_USER
    }, status = 200)