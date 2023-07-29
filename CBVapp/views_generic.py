from .models import Course,CourseSerializer
from rest_framework import mixins, generics

# Create your views here.
# class CourseListView(generics.ListAPIView, generics.CreateAPIView):
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
        