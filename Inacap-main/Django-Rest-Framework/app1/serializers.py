from dataclasses import field
from rest_framework import serializers
from app1.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CarreerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreer
        field = '__all__'        
        read_only_fields = ('cantidad')