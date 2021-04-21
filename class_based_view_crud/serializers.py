from rest_framework import serializers
from .models import Student


def age_validator(value):
    if value<18:
        raise serializers.ValidationError('age must be greater than 18')


class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(validators=[age_validator])    # validator

    # field level va;idation
    def validate_age(self, value):
        if value > 1000:
            raise serializers.ValidationError('Invalid roll number')
        return value

    # object level validation
    def validate(self, data):
        name = data.get('name')
        age = data.get('age')

        if name.lower() == 'Raj' and age != 20:
            raise serializers.ValidationError('age of raj must be 20')

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
