from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .auth import AuthHandlerIns


from .models import User
import jwt, datetime
# Create your views here.

class Faculty(APIView):
    def post(self, request):
        print('hi')
        User.create_user(self,username=request.data['username'],password=request.data['password'])
        return Response({"message":"done"})
    
    def get(self, request):
        print('hello')
        u=User.get_user(self)
        return Response({"message":"done","u":u})


@api_view(['POST'])
def login(request):
    u=User.get_user(request,username=request.data['username'])
    if u:
        k=AuthHandlerIns.verify_password(plain_password=request.data['password'],hashed_password= u['password'])
        if k:
            payload={
                'id':'',
                'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow(),
                'super':False,
                'faculty':True,
            }
            token = AuthHandlerIns.get_token(payload)
            return Response({"token":token})

    
    return Response({"message":"Nope"})
