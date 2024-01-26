from rest_framework import serializers
from RealmatriX.models import properties
from RealmatriX.models import users
from RealmatriX import models

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = properties
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'

class UserMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'password']

        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }