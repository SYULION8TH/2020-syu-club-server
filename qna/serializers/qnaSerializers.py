<<<<<<< HEAD:qna/serializers/qna_serializers.py
=======
from user.models import ClubsQna
from rest_framework import serializers

class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubsQna
        field = '__all__'
>>>>>>> b31b7653b082706c713ce9828b72ba7cbd5f0f34:qna/serializers/qnaSerializers.py
