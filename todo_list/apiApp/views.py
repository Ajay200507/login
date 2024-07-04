from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password

from apiApp.models import user_cred

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def login(request,format=None):
    username = request.data['username']
    password = request.data['password']

    # get method is used to give error when we put wrong login info
    try:
        user_get = user_cred.objects.get(username = username)
    except:
        return Response({'message':'user does not exit'})    


    if(check_password(password,user_get.password)):
        return Response({
            'messege':'successfully logined',
        })
    else:
        return Response({
            'messege':'wrong credential',
        })
    


# @api_view(['POST'])
# def create_user(request,format=None):
#     user = request.data['username']
#     password = request.data['password']
#     enc_pass = make_password(password)
    
#     obj = user_cred(
#         username = user,
#         password = enc_pass
#     )
#     obj.save()

#     return Response({'message':'user created'})


    # makepassword and checkpassword
