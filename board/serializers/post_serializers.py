from user.models import Posts, PostsLike, PostsReplies
from rest_framework import serializers
from board.serializers.post_replies_serializers import PostsRepliesSerializer
from django.contrib.auth.models import AnonymousUser


class PostsSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(read_only = True)
    views = serializers.IntegerField(read_only = True)
    user_like = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Posts
        Postsreplies = PostsRepliesSerializer
        fields =  '__all__' 
        read_only_fields = ['user', 'club', 'is_deleted']

    def get_user_like(self, instance):
        # 정보를 요청한 유저의 id를 가져온다.
        user =  self.context['request'].user
        # 로그인을 한 유저가 아닐 경우 전부 false를 반환한다.
        if type(user) == AnonymousUser:
            return False
        # 객체마다 유저가 like를 했는지 확인한다.
        if instance.like.filter(user = user).exists():
            return True
        else:
            return False


# 좋아요
class PostsLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostsLike
        fields = '__all__'







