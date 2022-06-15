from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, filters


from .serializers import ProjectSerializer, UserSerializer, PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from supervisor.models import Project, User, Post, Comment


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        pass


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        pass