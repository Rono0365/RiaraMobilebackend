from rest_framework import serializers
from django.contrib.auth.models import User
from noticeboard.models import Post
#from noticeboard.models import Student

class PostSerializer(serializers.ModelSerializer):
    firstname = serializers.ReadOnlyField(source='owner.first_name')
    lastname = serializers.ReadOnlyField(source='owner.last_name')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'body','firstname','lastname','poster']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username','firstname','lastname', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user