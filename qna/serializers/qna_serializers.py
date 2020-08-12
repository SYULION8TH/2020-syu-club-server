from .models import Qna
from rest_framework import serializers

class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qna
        field = ['id', 'title', 'body', 'comment']