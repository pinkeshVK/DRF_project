from django.shortcuts import render
from  .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


class StudentApi(viewsets.ViewSet):
    def list(self,request):

        print("====================================")
        print('Basename ', self.basename)
        print('action ',self.action)
        print('suffix : ', self.suffix)
        print('detail :', self.detail)
        print('name : ', self.name)
        print('description : ', self.description)

        stu = Student.objects.all()
        serializers = StudentSerializers(stu,many=True)
        return Response(serializers.data)

    def retrieve(self,request,pk=None):
        id = pk
        stu = Student.objects.get(id=id)
        serializers = StudentSerializers(stu)
        return Response(serializers.data)

    def create(self,request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)