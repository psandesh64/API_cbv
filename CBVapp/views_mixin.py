from .models import Course,CourseSerializer
from rest_framework import mixins, generics

# Create your views here.
class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class CourseDetailView(generics.GenericAPIView, 
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request,pk):
        return self.retrieve(request, pk)

    def put(self,request,pk):
        return self.update(request, pk)
        
    def delete(self,request,pk):
        return self.destroy(request, pk)
        