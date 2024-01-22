from rest_framework import serializers
from RealmatriX.models import properties
from RealmatriX.models import users

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = properties
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'