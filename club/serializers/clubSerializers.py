from user.models import Clubs, Posts, PostsLike
from rest_framework import serializers
from django.shortcuts import get_object_or_404


class ClubsSerializer(serializers.ModelSerializer):
    club_type = serializers.CharField(source = 'club_type.club_type_name')
    club_type_desc = serializers.CharField(source = 'club_type.club_type_desc')
    class Meta:
        model = Clubs
        fields = ['club_id','club_name','club_desc','club_type','club_img_url','club_logo_url','established', 'club_type_desc']

class FamousClubSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField()

    class Meta:
        model = Clubs
        fields = '__all__'
