from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course,CourseSerializer
from rest_framework import status
from django.http import Http404

# Create your views here.
class CourseListView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class CourseDetailView(APIView):
    def get_course(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    def get(self, request, pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request, pk):
        course = self.get_course(pk)
        courseserializer = CourseSerializer(course, data=request.data)
        if courseserializer.is_valid():
            courseserializer.save()
            return Response(courseserializer.data)
        return Response(courseserializer.errors)