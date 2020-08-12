from django.shortcuts import render, get_object_or_404
from .serializers import InfoSerializer, SocialSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
import json

class InfoGenerics(APIView):

    def get(self, request):
        user = get_object_or_404(User, pk=self.request.user.id)
        serializer = InfoSerializer(user)
        social_serializer = SocialSerializer(user.socialaccount_set, many=True)
        print(user.socialaccount_set.all()[0].get_avatar_url())
        return Response({
            "user": serializer.data,
            "user_profile": social_serializer.data
        },status=status.HTTP_200_OK)
