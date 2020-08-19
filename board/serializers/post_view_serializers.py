from rest_framework import serializers
from user.models import PostsViews
class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsViews
        fields = '__all__'