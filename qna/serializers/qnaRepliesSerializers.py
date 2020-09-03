from user.models import QnaReplies
from rest_framework import serializers
from django.contrib.auth.models import User

class RecursiveSerializer(serializers.Serializer): #RecursiveSerializer
	def to_representation(self, instance): #오버라이딩
		serializer = self.parent_reply.parent_reply.__class__(instance, context = self.context) #self.__class__로 직렬화
		return serializer.data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class QnaRepliesSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = QnaReplies
        fields = '__all__'
        read_only_fields = ['user', 'question', 'is_deleted', 'created_at', 'updated_at']
    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True) #self.__class__로 직렬화 #instance.reply를 통해 재귀
        serializer.bind('', self) #직렬화된 필드를 부모필드에 연결
        return serializer.data
