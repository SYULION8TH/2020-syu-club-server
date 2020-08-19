from user.models import QnaReplies
from rest_framework import serializers

class QnaRepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnaReplies
        fields = '__all__'