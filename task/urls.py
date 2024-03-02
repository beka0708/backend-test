from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.PostCreateAPIView.as_view()),
    path("comment/", views.CommentCreateAPIView.as_view()),
    path("like/", views.LikeCreateAPIView.as_view()),
    path("dislike/", views.DislikeCreateAPIView.as_view()),
    path("token/", views.MyTokenObtainPairView.as_view()),
]
