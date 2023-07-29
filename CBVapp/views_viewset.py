from .models import Course,CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.viewsets import ViewSet

# Create your views here.
# class CourseListView(generics.ListAPIView, generics.CreateAPIView):
class CourseViewSet(ViewSet):
    def list(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self,request,pk):
        try:
            courses = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(courses)
        return Response(serializer.data)
    
    def update(self,request,pk):
        course = Course.objects.get(pk=pk)
        courseserializer = CourseSerializer(course, data=request.data)
        if courseserializer.is_valid():
            courseserializer.save()
            return Response(courseserializer.data)
        return Response(courseserializer.errors)
    
    def destroy(self, request, pk):
        Course.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)