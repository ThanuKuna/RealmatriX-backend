from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from RealmatriX.serializers import PropertiesSerializer
from RealmatriX.models import Properties

@csrf_exempt
def propertiesApi(request,id=0):
    if request.method=='GET':
        property = Properties.objects.all()
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
        property=Properties.objects.get(id=id)
        property_serializer=PropertiesSerializer(property,data=property_data)
        if property_serializer.is_valid():
            property_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        property=Properties.objects.get(id=id)
        property.delete()
        return JsonResponse("Deleted Successfully",safe=False)

