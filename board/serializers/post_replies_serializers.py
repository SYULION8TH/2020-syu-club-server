from user.models import PostsReplies, UsersAdditionalInfo
from django.contrib.auth.models import User
from rest_framework import serializers

#to_representation을 오버라이딩 해서 화면에 출력
class RecursiveSerializer(serializers.Serializer):
	def to_representation(self, instance):
		serializer = self.parent_reply.parent_reply.__class__(instance, context = self.context)
		return serializer.data

class RepliesUser(serializers.ModelSerializer):
    name = serializers.CharField(source='add_info.name')
    profile = serializers.CharField(source='add_info.profile')
    class Meta:
        model = User
        fields = ['id', 'name', 'profile']
class PostsRepliesSerializer(serializers.ModelSerializer): 
    reply = serializers.SerializerMethodField(read_only= True)
    user = RepliesUser(read_only=True)
    class Meta:
        model = PostsReplies
        fields = '__all__'
        read_only_fields= ['user', 'post', 'is_deleted']

    def get_reply(self, instance):
        #self.__class__로 직렬화
        #instance.reply를 통해 재귀
        serializer = self.__class__(instance.reply, many=True)
        #직렬화된 필드를 부모필드에 연결
        serializer.bind('', self)
        return serializer.data
