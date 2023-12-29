from rest_framework import serializers
from RealmatriX.models import properties

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = properties
        fields = '__all__'