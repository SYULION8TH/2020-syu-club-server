from user.models import ClubsQna
from rest_framework import serializers
from qna.serializers import qnaRepliesSerializers

class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubsQna
        QnaReplies = qnaRepliesSerializers
        fields = '__all__'
