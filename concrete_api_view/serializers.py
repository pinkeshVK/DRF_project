from .models import Student
from rest_framework.serializers import Serializer
from rest_framework import serializers


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['age']
