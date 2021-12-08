from rest_framework import serializers
from .models import Student
from .models import Unit
from .models import Course
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name','last_name','School','id_no','Course','valid_till']


class unitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['unit_name','School','location','duration','Topic','day_taught','time_taught','assignment','assignment_till','valid_till']


class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['units','valid_till']
