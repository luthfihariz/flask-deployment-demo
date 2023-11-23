import jwt, os

def decode_jwt(token):   
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        print("Expired signature error")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token error")
        return None