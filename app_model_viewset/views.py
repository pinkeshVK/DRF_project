from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets

# Create your views here.


class StudentModelViewSet(viewsets.ModelViewSet): # or youcanuse ReadOnlyModelViewSet for get and retrive operations only, viewsets.ReadOnlyModelViewSet
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

