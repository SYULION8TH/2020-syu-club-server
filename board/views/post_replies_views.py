from django.shortcuts import render
from user.models import PostsReplies
from rest_framework import generics, viewsets 
from board.serializers.post_replies_serializers import PostsRepliesSerializer

class PostsRepliesList(generics.ListCreateAPIView): # 댓글
    serializer_class = PostsRepliesSerializer
    queryset = PostsReplies.objects.filter(parent_reply=None)

class PostsRepliesDetailGenerics(generics.RetrieveUpdateDestroyAPIView): 
    queryset = PostsReplies.objects.filter 
