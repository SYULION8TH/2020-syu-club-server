from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from board.views import post_views, post_replies_views, post_view_views
from board.serializers import post_serializers, post_replies_serializers

urlpatterns = [
    path('posts/', post_views.PostList.as_view()), #게시물 목록
    path('posts/<int:pk>', post_views.PostDetailGenerics.as_view()), #게시물 상세보기
    path('posts/<int:pk>/postreplies/', post_replies_views.PostsRepliesList.as_view()),
    path('posts/<int:pk>/post-view', post_view_views.PostsViewAPIView.as_view())
]




    


# urlpatterns = format_suffix_patter
