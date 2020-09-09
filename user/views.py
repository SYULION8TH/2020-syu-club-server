from django.shortcuts import render, get_object_or_404
from .serializers import InfoSerializer, AdditionalInfoSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser
import json

class InfoGenerics(APIView):

    def get(self, request):
        if type(request.user) == AnonymousUser:
            return Response("Please Login First", status=status.HTTP_401_UNAUTHORIZED)
        user = get_object_or_404(User, pk=self.request.user.id)
        serializer = InfoSerializer(user)
        if user.is_superuser == True:
            return Response({"user": serializer.data}, status = status.HTTP_200_OK)
        social_serializer = AdditionalInfoSerializer(user.add_info)
        return Response({
            "user": serializer.data,
            "user_profile": social_serializer.data
        },status=status.HTTP_200_OK)
