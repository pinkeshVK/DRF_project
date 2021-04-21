from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)    # person can't update name using ap only can post and get but can't put
    # put rqst will but but same will saty in DB only other fields will change
    class Meta:
        model = Student
        fields = ['name', 'age']  # mention fields which are required
        # write_only_fields = ['name'] same as first name line
        #extra_kwargs = {'name': {'read_only': True,'required':True}}
