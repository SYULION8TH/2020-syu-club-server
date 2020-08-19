from user.models import ClubsQna
from rest_framework import serializers

class QnaSerializer(serializers.ModelSerializer):
    # qnareplies = qnaCommentSerializers.QnaRepliesSerializer(many=True)

    class Meta:
        model = ClubsQna
        fields = '__all__'
