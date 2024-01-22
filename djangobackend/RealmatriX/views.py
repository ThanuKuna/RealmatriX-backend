from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from RealmatriX.serializers import PropertiesSerializer,UserSerializer
from RealmatriX.models import properties,users

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

