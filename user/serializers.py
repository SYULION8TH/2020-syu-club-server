from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class ClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clubs
        fields='__all__'


class InterestClubSerializer(serializers.ModelSerializer):
    club = ClubsSerializer()
    class Meta:
        model = models.RelInterestClub
        exclude = ['updated_at', 'user']

class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsersAdditionalInfo
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    interest_club = InterestClubSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff','interest_club']