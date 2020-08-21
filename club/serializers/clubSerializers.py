from user.models import Clubs, Posts, PostsLike
from rest_framework import serializers
from django.shortcuts import get_object_or_404


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsLike
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    like = PostLikeSerializer(many=True)
    class Meta:
        model = Posts
        fields = '__all__'

class ClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ['club_id','club_name','club_desc','club_type','club_img_url','club_logo_url','established']

class FamousClubSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField()

    class Meta:
        model = Clubs
        fields = '__all__'
