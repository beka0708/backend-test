from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Post, Comment, Like
from .serializers import (
    PostSerializer,
    CommentSerializer,
    LikeSerializer,
    MyTokenObtainPairSerializer,
)

# from django_filters.rest_framework import DjangoFilterBackend
#
#
# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['created_at', 'author', 'likes__isnull']


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.request.data.get("post")
        if Like.objects.filter(user=user, post_id=post_id).exists():
            raise ValidationError("You have already reacted to this post.")
        serializer.save(user=user)


class DislikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.request.data.get("post")
        if Like.objects.filter(user=user, post_id=post_id, is_dislike=True).exists():
            raise ValidationError("You have already disliked this post.")
        serializer.save(user=user, is_dislike=True)
