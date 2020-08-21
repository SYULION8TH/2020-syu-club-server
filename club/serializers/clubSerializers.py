from user.models import Clubs, Posts, PostsLike
from rest_framework import serializers
from django.shortcuts import get_object_or_404


class ClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ['club_id','club_name','club_desc','club_type','club_img_url','club_logo_url','established']



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsLike
        fields = '__all__'


class FClubSerializer(serializers.Serializer):
    club = serializers.SerializerMethodField()
    like_count = serializers.IntegerField()

    def get_club(self, obj):
        club = get_object_or_404(Clubs, pk = obj["club_id"])
        serializer = ClubsSerializer(club)
        serializer.bind('',self)
        return serializer.data