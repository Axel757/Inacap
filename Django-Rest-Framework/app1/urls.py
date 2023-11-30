from django.urls import path, include
from app1.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('students', StudentViewSets)
    


urlpatterns = [
    
    path('employees/', employeeView, name='employees'),
    
    
    # FUNCTION BASED VIEWS =================================================
    
    # path('students/', student_list, name='students'),
    # path('students/<int:pk>', student_detail, name='students/<pk>'),
    
    # =================================================================    
    
    #CLASS BASED VIEWS & MIXINS=================================    
    
    # path('students/', StudentList.as_view(), name='students'),
    # path('students/<int:pk>', StudentDetail.as_view, name='students/<pk>'),    
    
    # =================================================================
    
    
    #VIEW SETS =================================================
    
    path("", include(router.urls))
    
    
    # ==========================================================
]
