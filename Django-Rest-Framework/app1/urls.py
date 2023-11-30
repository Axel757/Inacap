from django.urls import path, include
from app1.views import *
urlpatterns = [
    path('employees/', employeeView, name='employees'),
    # path('students/', student_list, name='students'),
    # path('students/<int:pk>', student_detail, name='students/<pk>'),
    
    path('students/', StudentList.as_view(), name='students'),
    path('students/<int:pk>', StudentDetail.as_view, name='students/<pk>'),    
]
