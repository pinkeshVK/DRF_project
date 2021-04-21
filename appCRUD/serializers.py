
from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        #print(instance.name)
        instance.age = validated_data.get('age', instance.age)
        #instance.save()
        return instance
