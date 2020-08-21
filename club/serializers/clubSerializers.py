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
    club_posts = PostSerializer(many=True)
    post_count = serializers.IntegerField()
    class Meta:
        model = Clubs
        fields = ['club_id','club_name','club_desc','club_type','club_img_url','club_logo_url','established','club_posts', 'post_count']







class FClubSerializer(serializers.Serializer):
    club = serializers.SerializerMethodField()
    like_count = serializers.IntegerField()

    def get_club(self, obj):
        club = get_object_or_404(Clubs, pk = obj["club_id"])
        serializer = ClubsSerializer(club)
        serializer.bind('',self)
        return serializer.data