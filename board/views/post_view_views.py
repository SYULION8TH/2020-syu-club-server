from user.models import PostsViews, Posts
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from board.serializers.post_view_serializers import PostViewSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
from datetime import datetime, timedelta


class PostsViewAPIView(APIView):
    def get(self,request, pk):

        # 요청자의 ip를 보내준다.
        return Response("changed", status = status.HTTP_200_OK)
