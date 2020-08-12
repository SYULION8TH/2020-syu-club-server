from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class InterestClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RelInterestClub
        fields = '__all__'
class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsersAdditionalInfo
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    interest_club = InterestClubSerializer
    class Meta:
        model = User
        fields = ['id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff','interest_club']