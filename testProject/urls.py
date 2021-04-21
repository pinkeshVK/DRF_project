from django.contrib import admin
from django.urls import path, include
from app1.views import home_views, about_views, contact_views
from app2.views import student_detail_views, student_all_views, post_views
from appCRUD.views import student_api
from class_based_view_crud import views
from app_model_serializer.views import student_api
from app_generics import views
from app_group_generics import views
from concrete_api_view.views import StudentList, StudentRetrieve, StudentRetrieveUpdateDestroy
from app_viewset.views import StudentApi
from app_model_viewset.views import StudentModelViewSet
from app_authentication.views import StudentSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from app_authentication.token import CustomAuthToken

# create router object
router = DefaultRouter()
router1 = DefaultRouter()
router2 = DefaultRouter()

# Register viewset class from views to router
router.register('studentapi',StudentApi, basename='student')
router1.register('studentmodelapi', StudentModelViewSet, basename='studentmodel')
router2.register('studentset', StudentSet, basename='studentset')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views, name='home'),
    path('about/', about_views),
    path('contact/', contact_views),
    path('app2/<int:id>', student_detail_views),  # add id number after /... like app2/1
    path('app2/all/', student_all_views),
    path('app2/post/', post_views),
    path('api/', student_api),
    # path('api2/', views.StudentAPI.as_view()),
    path('api3/', student_api),
   # path('list/', views.StudentList.as_view()),
  #  path('retrieve/<int:pk>', views.StudentRetrieve.as_view()),
   # path('create/', views.StudentCreate.as_view()),
    #path('update/<int:pk>', views.StudentUpdate.as_view()),
    #path('destroy/<int:pk>',views.StudentDestroy.as_view()),
    path('lc/', views.StudentListAndCreate.as_view()),                 # group generics app view
    path('rud/<int:pk>', views.StudentRetrieveUpdateDelete.as_view()),        # group generics app view

    path('api/list',StudentList.as_view()),                         # concrete api views urls
    path('api/retrieve/<int:pk>',StudentRetrieve.as_view()),
    path('api/rud/<int:pk>',StudentRetrieveUpdateDestroy.as_view()),
    path('', include(router.urls)),
    path('modelviewset/', include(router1.urls)),
    path('studentset/', include(router2.urls)),
    path('auth/', include('rest_framework.urls')),  # for session auth, it will give a login button on top right on browser aftr hitting url
    path('gettoken/', obtain_auth_token),
    path('gettoken/', CustomAuthToken.as_view()),


]
