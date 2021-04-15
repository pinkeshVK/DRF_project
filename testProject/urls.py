"""testProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import home_views,about_views,contact_views
from app2.views import student_detail_views,student_all_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_views,name='home'),
    path('about/',about_views),
    path('contact/',contact_views),
    path('app2/<int:id>',student_detail_views),  # add id number after /... like app2/1
    path('app2/all/',student_all_views),

]
