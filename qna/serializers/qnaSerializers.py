from user.models import ClubsQna
from rest_framework import serializers
from qna.serializers import qnaRepliesSerializers

class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubsQna
        # QnaReplies = qnaRepliesSerializers
        fields = '__all__'
        read_only_fields = ['created_at', 'user', 'is_deleted', 'club', 'updated_at']
