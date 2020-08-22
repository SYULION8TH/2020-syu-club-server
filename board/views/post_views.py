from django.shortcuts import render
from user.models import Posts, PostsLike
from rest_framework import generics, viewsets
#경로를 표시하기 위해서는 . 단일파일이 아닌 폴더 형태기 때문에 경로 표시 필수
from board.serializers.post_serializers import PostsSerializer, PostsLikeSerializer, LikeSerializer
#filter을 사용
from django_filters.rest_framework import DjangoFilterBackend, FilterSet


#filter(9-19) //genrics
class PostFilter(FilterSet):
    class Meta:
        model = Posts
        #post_title //'exact'는 정확한 title입력 'contains'는 post_title이 포함된 결과물 모두 표시
        fields = {'post_title':['exact', 'contains']}

class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    # serializer_class = PostsSerializer
    serializer_class = LikeSerializer
    # filter_class = PostFilter
    filterset_class = PostFilter
    filter_backends = [DjangoFilterBackend]

# post detail
class PostDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class PostsLikeGenerics(generics.CreateAPIView):
    queryset = PostsLike.objects.all()
    serializer_class = PostsLikeSerializer

class PostsLikeGenerics(generics.DestroyAPIView):
    queryset = PostsLike.objects.all()
    serializer_class = PostsLikeSerializer