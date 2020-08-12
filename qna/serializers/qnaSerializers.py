from user.models import ClubsQna
from rest_framework import serializers

class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubsQna
        field = '__all__'