from user.models import Posts, PostsLike, PostsReplies
from rest_framework import serializers
from board.serializers.post_replies_serializers import PostsRepliesSerializer

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        Postsreplies = PostsRepliesSerializer
        fields =  '__all__' 

# 좋아요
class PostsLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsLike
        fields = '__all__'




