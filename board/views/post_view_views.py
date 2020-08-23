from user.models import PostsViews, Posts
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from board.serializers.post_view_serializers import PostViewSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
from datetime import datetime, timedelta

# 요청자의 ip를 가져온다.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class PostsViewAPIView(APIView):
    def get(self,request, pk):
        # 현재시간
        now = datetime.now()
        # 현재에서 1시간 전
        yesterday = now - timedelta(hours=1)
        # 1시간 사이의 조회자들을 가져온다.
        postViews = PostsViews.objects.filter(checked_at__range = [yesterday, now], post=pk)
        # 1시간 사이의 조회 데이터를 살피고 1시간 내에 조회한 기록이 있으면 조회수를 추가하지 않는다.
        for item in postViews:
            if item.user_ip == get_client_ip(request):
                return Response("already read posts", status = status.HTTP_200_OK)
        # 1시간 사이의 조회 데이터를 살피고 조회한 기록이 없으면 조회수 추가
        # 조회 데이터를 생성하기 위해 새로운 조회 객체 생성
        postView = PostsViews()
        # 객체의 post필드에 조회한 게시물 넣기
        # posts/:pk/view url 경로를 통해 pk 가져오기
        postView.post = get_object_or_404(Posts, pk = pk)
        # 로그인한 유저가 아니라면 객체의 유저 필드를 비워둔다.
        if type(request.user) == AnonymousUser:
            postView.user = None
        else:
            # 로그인한 유저라면 요청한 유저를 객체의 유저 필드에 넣는다.
            postView.user = self.request.user
        # 요청자의 ip를 기록한다.
        postView.user_ip = get_client_ip(request)
        # 만든 객체를 저장한다.
        postView.save()
        # 요청자의 ip를 보내준다.
        return Response(get_client_ip(request), status = status.HTTP_201_CREATED)
