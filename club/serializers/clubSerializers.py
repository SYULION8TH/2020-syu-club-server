from user.models import Clubs, Posts, PostsLike,RelInterestClub
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser


class ClubsSerializer(serializers.ModelSerializer):
    club_type = serializers.CharField(source = 'club_type.club_type_name')
    club_type_desc = serializers.CharField(source = 'club_type.club_type_desc', read_only = True)
    likes = serializers.IntegerField(read_only = True)
    user_like = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Clubs
        fields = '__all__'

    def current_user(self):
        print(self.context.get('request'))
        return self.context['request'].user
    def get_user_like(self, instance):
        # 정보를 요청한 유저의 id를 가져온다.
        user =  self.current_user()
        # 로그인을 한 유저가 아닐 경우 전부 false를 반환한다.
        if type(user) == AnonymousUser:
            return False
        # 객체마다 유저가 like를 했는지 확인한다.
        if instance.like_user.filter(user = user).exists():
            return True
        else:
            return False

class FamousClubSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField()

    class Meta:
        model = Clubs
        fields = '__all__'