from user.models import ClubsQna
from rest_framework import serializers
from qna.serializers import qnaCommentSerializers

class QnaSerializer(serializers.ModelSerializer):
    qnareplies = qnaCommentSerializers.QnaRepliesSerializer(many=True, read_only=True)

    class Meta:
        model = ClubsQna
        fields = '__all__'
