from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from RealmatriX.serializers import PropertiesSerializer,UserSerializer
from RealmatriX.models import properties,users
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.exceptions import AuthenticationFailed
from knox.auth import AuthToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render


@csrf_exempt
def propertiesApi(request,id=0):
    if request.method=='GET':
        property = properties.objects.all()
        property_serializer=PropertiesSerializer(property,many=True)
        return JsonResponse(property_serializer.data,safe=False)
    elif request.method=='POST':
        property_data=JSONParser().parse(request)
        property_serializer=PropertiesSerializer(data=property_data)
        if property_serializer.is_valid():
            property_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        property_data=JSONParser().parse(request)
        property=properties.objects.get(id=id)
        property_serializer=PropertiesSerializer(property,data=property_data)
        if property_serializer.is_valid():
            property_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        property=properties.objects.get(id=id)
        property.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


@csrf_exempt
def usersApi(request,id=0):
    if request.method=='GET':
        user = users.objects.all()
        users_serializer=UserSerializer(user,many=True)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method=='POST':
        users_data=JSONParser().parse(request)
        users_serializer=UserSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        users_data=JSONParser().parse(request)
        user=users.objects.get(id=id)
        users_serializer=UserSerializer(user,data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        user=users.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@api_view(['POST'])
def login_user(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        user = get_user_model().objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        _, token = AuthToken.objects.create(user)
        user.is_active = True
        user.save()
        return Response({
            'user_info': {
                'username': user.username,
                'password': user.password
            },
            'token': token
        }, status=status.HTTP_200_OK)
    except KeyError:
        return Response({
            "details": "error"
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_user(request):
    try:
        return Response({
            "details": "Token is valid"
        }, status=status.HTTP_200_OK)
    except KeyError:
        return Response({
            "details": "Token is invalid"
        }, status=status.HTTP_400_BAD_REQUEST)