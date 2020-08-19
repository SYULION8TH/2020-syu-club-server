from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from rest_framework.urlpatterns import format_suffix_patterns
from board.views import post_views, post_replies_views
from board.serializers import post_serializers, post_replies_serializers

urlpatterns = [
    path('posts/', post_views.PostList.as_view()), #게시물 목록
    path('posts/<int:pk>', post_views.PostDetailGenerics.as_view()), #게시물 상세보기
    path('posts/<int:pk>/postreplies/', post_replies_views.PostsRepliesList.as_view()),

=======
from board.views.post_view_views import PostsViewAPIView


urlpatterns = [
    path('posts/<int:pk>/post-view', PostsViewAPIView.as_view())
>>>>>>> 180cb13419eb240d437f229c2a8f841532599169
]

# urlpatterns = format_suffix_patter
