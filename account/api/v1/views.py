from django.http import request
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import*
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

User = get_user_model()

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def start(request):
    user = get_user_model()
    users = user.objects.all()
    return Response(data={'message':'hello'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def signup(request):
    if request.method == "POST":
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(
                data=[
                user.data,
                {'token':Token.objects.get(user__username=user.data.get('username')).key}
                ],
                status=status.HTTP_201_CREATED)
        else:
            return Response(data=user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request, **kwargs):
    if kwargs:
        user = User.objects.filter(username=kwargs['un'])
    else: 
        user = User.objects.filter(email=request.user)
        
    if user.exists():
        
        ser_user = UserSerializer(instance=user.first())
        return Response(data=ser_user.data, status=status.HTTP_200_OK)
    else:   
        return Response(
            data={"message":"we didn't find user with this username in our database"},
            status=status.HTTP_400_BAD_REQUEST
            )

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])

def delete_user(request):
    response = {}
    try:
        user = User.objects.get(email=request.user)
        user.delete()
        response['data'] = {'message':'user deleted'}
        response['status'] = status.HTTP_200_OK
    except Exception as e:
        response['data'] = {'message':f'error while delete {e}'}
        response['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**response)

@api_view(['PUT', 'GET'])
@permission_classes([IsAuthenticated])

def user_update(request):
    try:
        user = User.objects.get(email=request.user)
    except Exception as e:
        return Response(data={'message':f'error {e}'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        ser_user = UserSerializer(data=request.data, instance=user)        
        if ser_user.is_valid():
            ser_user.save()
            return Response(data=ser_user.data, status=status.HTTP_200_OK)
        else:
            return Response(data=ser_user.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='GET':
        ser_user = UserSerializer(instance=user)
        return Response(data=ser_user.data, status=status.HTTP_200_OK)

class UserViewSets(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def details(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, username=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['DELETE'])
def logout(request):
    try:
        # request.user.auth_token.delete()
        Token.objects.get(user__email=request.user)
    except Exception as e:
        return Response(data={'erroe':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'message':'successfully logout'},status=status.HTTP_204_NO_CONTENT)