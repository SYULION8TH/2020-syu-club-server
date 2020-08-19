from user.models import PostsViews, Posts
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from board.serializers.post_view_serializers import PostViewSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
from datetime import datetime, timedelta


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class PostsViewAPIView(APIView):
    def get(self,request, pk):
        flag = False
        now = datetime.now()
        yesterday = now - timedelta(hours=1)
        postViews = PostsViews.objects.filter(checked_at__range = [yesterday, now])
        print(postViews)
        postView = PostsViews()
        postView.post = get_object_or_404(Posts, pk = pk)
        if type(request.user) == AnonymousUser:
            postView.user = None
        else:
            postView.user = self.request.user
        postView.user_ip = get_client_ip(request)
        for item in postViews:
            if item.user_ip == get_client_ip(request):
                flag = True

        if flag:
            return Response("already read posts", status = status.HTTP_200_OK)
        else:
            postView.save()
            return Response(get_client_ip(request), status = status.HTTP_201_CREATED)
