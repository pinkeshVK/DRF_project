from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer, JSO


# Create your views here.

def student_detail_views(request, id):  # id as arg to pass from url of browser like /2, urls.py make changes in pattern
    stu = Student.objects.get(id=id)
    # print(f"the stu from models is {stu} ")
    serializer = StudentSerializers(stu)
    # print(f"serializer is {serializer} ")
    json_data = JSONRenderer().render(serializer.data)                 # for alternate method no need of this line just after line 13 GOTO line 17
    # print(f"serializer.data is {serializer.data} and json_data is {json_data}")
    return HttpResponse(json_data, content_type='application/json')    # alternate method : return Jsonresponse(serializer.data)


def student_all_views(request):
    qs = Student.objects.all()
    print(f"the stu from models is {qs} ")
    serializer = StudentSerializers(qs, many=True)
    print(f"serializer is {serializer} ")
    json_data = JSONRenderer().render(serializer.data)                          # for alternate method no need of this line just after line 13 GOTO line 17
    print(f"serializer.data is {serializer.data} and json_data is {json_data}")
    return HttpResponse(json_data, content_type='application/json')             # alternate method : return Jsonresponse(serializer.data,safe = false)
                                                                                # becoz we are getting qs which is collection of objects not dict
                                                                                #if we are getting dictionary then lik abouve function we should leave it like default of safe=true

