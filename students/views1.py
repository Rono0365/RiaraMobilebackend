#from django.shortcuts import render
from rest_framework import generics
from students import serializers
from .models import Student
from .models import Unit
from .models import Course
#from django.contrib.auth.models import User
# Create your views here.
class PostListx(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.UserSerializer
    def perform_create(self, serializer):
        serializer.save(first_name=self.request.user)
class unitListx(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = serializers.unitSerializer
    def perform_create(self, serializer):
        serializer.save()
class unitDetailx(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = serializers.unitSerializer
class courseListx(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.courseSerializer
    def perform_create(self, serializer):
        serializer.save()
class PostDetailx(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.UserSerializer
