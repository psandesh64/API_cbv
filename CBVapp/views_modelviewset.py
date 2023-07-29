from .models import Course,CourseSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet

# Create your views here.
# class CourseListView(generics.ListAPIView, generics.CreateAPIView):
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
