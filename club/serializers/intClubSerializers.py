from user.models import RelInterestClub, Clubs
from rest_framework import serializers



class IntClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelInterestClub
        # fields = ['club','created_at']
        fields = '__all__'

