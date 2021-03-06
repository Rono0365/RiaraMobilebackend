from rest_framework import serializers
from django.contrib.auth.models import User
from noticeboard.models import Post
from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import APIException
#from noticeboard.models import Student
from rest_framework.validators import UniqueValidator
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PostSerializer(serializers.ModelSerializer):
    firstname = serializers.ReadOnlyField(source='owner.first_name')
    lastname = serializers.ReadOnlyField(source='owner.last_name')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'body','firstname','lastname','poster']
        
class RegisterSerializer(serializers.ModelSerializer,):
    permission_classes = []
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username','phone_no','programme','shift','academic_docs']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
           user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_no=validated_data['phone_no'],
            programme=validated_data['programme'],
            shift=validated_data['shift'],
            academic_docs=validated_data['academic_docs']
        )
           user.set_password(validated_data['password'])
           user.save()
           return user