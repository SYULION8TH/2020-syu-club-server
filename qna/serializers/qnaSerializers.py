from user.models import ClubsQna
from rest_framework import serializers
from qna.serializers import qnaRepliesSerializers
from django.contrib.auth.models import User
# from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class QnaSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = serializers.IntegerField(read_only = True)
    class Meta:
        model = ClubsQna
        fields = '__all__'
        read_only_fields = ['created_at', 'user', 'is_deleted', 'club', 'updated_at']
