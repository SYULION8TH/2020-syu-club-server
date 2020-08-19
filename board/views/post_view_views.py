from user.models import PostsViews, Posts
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from board.serializers.post_view_serializers import PostViewSerializer
from django.shortcuts import get_object_or_404


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class PostsViewAPIView(APIView):
    def get(self,request, pk):
        postView = PostsViews()
        print(pk)
        postView.post = get_object_or_404(Posts, pk = pk)
        if self.request.user:
            postView.user = self.request.user
        postView.user_ip = get_client_ip(request)
        postView.save()

        return Response(get_client_ip(request), status = status.HTTP_201_CREATED)
