from rest_framework import serializers
from app1.models import *

class StudenSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = '__all__'