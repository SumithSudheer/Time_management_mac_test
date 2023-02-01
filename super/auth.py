from passlib.context import CryptContext
from datetime import datetime, timedelta
from mactest.settings import SECRET_KEY
import jwt


class AuthHandler():
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    secret =SECRET_KEY

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_token(self, payload):
        return jwt.encode(payload,SECRET_KEY,algorithm='HS256')

def is_auth_jwt(request):
    try:
        token = request.headers['Authorization'].split(' ')
        token = token[1]
        try:
            k = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        except Exception as e:
            print(e)
            print('Timeout')
        else:
            return k
    except:
        return False

def is_super_admin(request):
    t=is_auth_jwt(request)
    if t:
        if t['super']:
            return True
        else:
            return False
    else:
        return False






AuthHandlerIns = AuthHandler()