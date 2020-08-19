from user.models import RelInterestClub
from rest_framework import serializers


class IntClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelInterestClub
        # fields = ['club','created_at']
        fields = '__all__'
