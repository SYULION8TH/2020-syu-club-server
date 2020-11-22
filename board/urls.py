from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from board.views import post_views, post_replies_views, post_view_views
from board.serializers import post_serializers, post_replies_serializers

urlpatterns = [
    path('posts', post_views.PostList.as_view()), #게시물 목록
    path('clubs/<int:pk>/posts',post_views.PostList.as_view()),#동아리별 게시물 목록
    path('clubs/<int:club_id>/posts/<int:pk>', post_views.PostDetailGenerics.as_view()), #게시물 상세보기
    path('posts/<int:pk>/replies', post_replies_views.PostsRepliesList.as_view()),
    path('posts/view', post_view_views.PostsViewAPIView.as_view()),
    path('posts/famous', post_views.FamousPostsGenerics.as_view()),
    path('posts/<int:pk>/likes',post_views.PostsLikesAPIView.as_view())   #working

]

# urlpatterns = format_suffix_patter
