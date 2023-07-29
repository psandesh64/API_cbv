from django.contrib import admin
from django.urls import path
# from CBVapp import views
# from CBVapp import views_mixin
from CBVapp import views_generic

urlpatterns =[
    path('courses', views_generic.CourseListView.as_view()),
    path('courses/<int:pk>', views_generic.CourseDetailView.as_view()),
]