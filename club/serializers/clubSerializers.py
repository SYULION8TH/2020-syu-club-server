from user.models import Clubs
from rest_framework import serializers


class ClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ['club_id','club_name','club_desc','club_type','club_img_url','club_logo_url','established']