from rest_framework import serializers
from RealmatriX.models import Properties

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'