from django.shortcuts import render
from rest_framework import generics
from noticeboard import serializers
from .models import Student
from django.contrib.auth.models import User
# Create your views here.
class PostListx(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)