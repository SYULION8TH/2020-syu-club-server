from django.shortcuts import render
from user.models import PostsReplies
from rest_framework import generics, viewsets 
from board.serializers.post_replies_serializers import PostsRepliesSerializer

class PostsRepliesList(generics.ListCreateAPIView): # 댓글
    serializer_class = PostsRepliesSerializer
    queryset = PostsReplies.objects.filter(parent_reply=None)

    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.kwargs.get('pk')
        qs = qs.filter(post=pk)

        return qs

class PostsRepliesDetailGenerics(generics.RetrieveUpdateDestroyAPIView): 
    queryset = PostsReplies.objects.filter 
