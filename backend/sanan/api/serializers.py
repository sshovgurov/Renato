from asyncore import read
from rest_framework import serializers, validators
from supervisor.models import Project, Post, Comment, User

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = User
        fields = ('username', 'bio', 'role', 'project',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    post = serializers.SlugRelatedField(slug_field='id', read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'post', 'text', 'created', 'author', )