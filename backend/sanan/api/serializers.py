from rest_framework import serializers, validators
from supervisor.models import Project, Post, Comment
from users.models import User


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"