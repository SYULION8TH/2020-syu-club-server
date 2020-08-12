from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialaccountSocialaccount
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    socialaccount_set = SocialSerializer
    class Meta:
        model = User
        fields = ['id', 'socialaccount_set']