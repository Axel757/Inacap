from django.shortcuts import render
from django.http import JsonResponse
from app1.models import *
from app1.serializers import * 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.
def employeeView(request):
    empleados = Employee.objects.all()
    
    emp = {
        'empleados': list(empleados.values('name', 'salary'))
    }
    
    return JsonResponse(emp)


# @api_view(['GET', 'POST'])
# def student_list(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def student_detail(request, pk):
#     try:
#         student = Student.objects.get(pk=pk)    
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#        serializer = StudentSerializer(student)
#        return Response(serializer.data)

#     if request.method == 'DELETE':
#        student.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)   
   
#     if request.method == 'PUT':
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class StudentList(APIView):
        def get(self, request):
            students = Student.objects.all()
            serializers = StudentSerializer(students, many=True)
            return Response(serializers.data)
        
        def post(self, request):
            serializers = StudentSerializer(data = request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
        def get_object(self, pk):
            try:
                return Student.objects.get(pk=pk)    
            except Student.DoesNotExist:
                return Http404
        
        def get(self, request, pk):
            student = self.get_object(pk)
            serializers = StudentSerializer(student)
            return Response(serializers.data)            
        
        def put(self, request, pk):
            student = self.get_object(pk)
            serializers = StudentSerializer(student, data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)      
        
        def delete(self, request, pk):
            student = self.get_object(pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
