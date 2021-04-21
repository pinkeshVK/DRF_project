import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        print(f"============={json_data}=======================")
        print(type(json_data))
        stream = io.BytesIO(json_data)
        print(stream)
        print(type(stream))
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        qs = Student.objects.all()
        serializer = StudentSerializers(qs, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializers(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'put':
        print("inside put")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)

        serializer = StudentSerializers(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'updated successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        print("inside del")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()

        res = {'msg': 'deleted successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')

