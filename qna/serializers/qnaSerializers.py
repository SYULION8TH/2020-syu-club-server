from user.models import ClubsQna
from rest_framework import serializers
from qna.serializers import qnaRepliesSerializers

class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubsQna
        QnaReplies = qnaRepliesSerializers
        fields = '__all__'
<<<<<<< HEAD
        # read_only_fields =
=======
        read_only_fields = ['created_at', 'user', 'is_deleted', 'club', 'updated_at']
>>>>>>> aaf47a07bcdad59fa6f04cf88008e6aa9b979a47
