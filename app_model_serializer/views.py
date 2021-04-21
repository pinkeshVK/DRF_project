from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .model_serializers import StudentSerializers
from rest_framework import status

# Create your views here.

# @api_view()  # by default get
# def func1(request):
#    return Response({'msg': 'Get working'})

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        id = request.data.get('id')
        print(id)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'posted'},status=status.HTTP_201_CREATED)

    return Response({'msg': 'Hey'})

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated'})
        return Response(serializer.errors)

