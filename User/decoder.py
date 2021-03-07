import jwt
from decouple import config

def tokenDecoder(token):
    try:
        token = token.replace("Bearer "," ").replace(" ","")
        return jwt.decode(token, config('SECRET_KEY'), algorithms=["HS256"]);
    except:
        return jwt.decode(token, config('SECRET_KEY'), algorithms=["HS256"]);