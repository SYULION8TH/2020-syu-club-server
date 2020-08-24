from user.models import QnaReplies
from rest_framework import serializers

class RecursiveSerializer(serializers.Serializer): #RecursiveSerializer
	def to_representation(self, instance): #오버라이딩
		serializer = self.parent_reply.parent_reply.__class__(instance, context = self.context) #self.__class__로 직렬화
		return serializer.data

class QnaRepliesSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField(read_only=True) 

    class Meta:
        model = QnaReplies
        fields = '__all__'
    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True) #self.__class__로 직렬화 #instance.reply를 통해 재귀
        serializer.bind('', self) #직렬화된 필드를 부모필드에 연결
        return serializer.data
