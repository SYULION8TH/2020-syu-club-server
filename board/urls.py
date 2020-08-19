from django.contrib import admin
from django.urls import path, include
from board.views.post_view_views import PostsViewAPIView


urlpatterns = [
    path('posts/<int:pk>/post-view', PostsViewAPIView.as_view())
]


