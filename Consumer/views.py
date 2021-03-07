# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

Consumer = get_user_model()

# ====================================== LOGIN ========================================================
@api_view(['POST'])
@permission_classes([AllowAny])
def get_tokens_for_user(request):

    username = request.POST.get("username")
    password = request.POST.get("password")

    user = Consumer.objects.get(username=username)
    
    if user is None:
        return Response({ "message": "Username found"}, status=400)

    if  user.check_password(password):

        tokens = user.token()
        
        return Response({
            'refresh': tokens['refresh'],
            'access': tokens['access'],
        }, status=201)

    else:
        return Response({"message":"Username and password did not match"}, status=400)
