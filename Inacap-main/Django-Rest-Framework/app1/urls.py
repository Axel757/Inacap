from base64 import urlsafe_b64decode
from django.urls import path, include
from app1.views import *
from rest_framework.routers import DefaultRouter


# estudianteRouter = DefaultRouter()
# estudianteRouter.register('students', StudentViewSets)
    
# carreraRouter = DefaultRouter()
# carreraRouter.register('carreer', CarreerViewSets)


urlpatterns = [
    
    path('employees/', employeeView, name='employees'),
    
    
    # FUNCTION BASED VIEWS =================================================
    
    # path('students/', student_list, name='students'),
    # path('students/<int:pk>', student_detail, name='students/<pk>'),
    
    # =================================================================    
    
    #CLASS BASED VIEWS & MIXINS=================================    
    
    path('students/', StudentList.as_view(), name='students'),
    path('students/<int:pk>', StudentDetail.as_view, name='students/<pk>'),    
    path('carreers/', CarreerList.as_view(), name='carreers'),
    path('carreers/<int:pk>', CarreerDetail.as_view, name='carreers/<pk>'),  
    # =================================================================
    
    
    #VIEW SETS =================================================
    
    # path("", include(estudianteRouter.urls)),
    # path("", include(carreraRouter.urls))
    
    
    # ==========================================================
]
