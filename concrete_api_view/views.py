from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView


# Create your views here.


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):  # and many more combination methods
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

