from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .custom_auth import CustomAuth
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions, \
    DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions
from .custom_permission import MyPermission
# Create your views here.


class StudentSet(viewsets.ModelViewSet): # or youcanuse ReadOnlyModelViewSet for get and retrive operations only, viewsets.ReadOnlyModelViewSet
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [BasicAuthentication]  #['SessionAuthentication'] , or customauth; in url write ../username=superuser or user1
    permission_classes = [IsAuthenticated] # or ['IsAdminUser']  for user created and set as staff user from admin panel
 # IsAuthenticatedReadOnly  also used for, if authenticated do all pperations if not authg then read only
# if DjangoModelPermissions is used thenwe will have to grand the add,change, read, delete permissions
# from django admin user from list or user permissions
# or use [MyPermission] from custom_permission.py file


# you can also define authentication in settings.py file type to apply that to all classes in views.py:
# REST_FRAMEWORK = {
#           'DEFAULT_AUTHENTICATION_CALSSES' :['rest_framework.authentication.BasicAuthentication'],
#           'DEFAULT_PERMISSION_CLASSES' : ['rest_framework.permissions.IsAuthenticated']
#           }

# we can also exclude perticular class from authentication if globally authentication is set for views by overriding,
# we can override the global authentiucation and permission also
