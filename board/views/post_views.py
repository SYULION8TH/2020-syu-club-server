from django.shortcuts import render
from django.http import Http404
from user.models import Posts, PostsLike
from rest_framework import generics, viewsets, mixins, status
from rest_framework.views import APIView
#경로를 표시하기 위해서는 . 단일파일이 아닌 폴더 형태기 때문에 경로 표시 필수
from board.serializers.post_serializers import PostsSerializer, PostsLikeSerializer
#filter을 사용
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import SearchFilter
from django.db.models import Count
from rest_framework.response import Response


#filter(9-19) //genrics
class PostFilter(FilterSet):
    class Meta:
        model = Posts
        #post_title //'exact'는 정확한 title입력 'contains'는 post_title이 포함된 결과물 모두 표시
        fields = {'post_title':['exact', 'contains']}

class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.annotate(likes= Count('like', distinct=True), views = Count('view', distinct=True)).all()
    serializer_class = PostsSerializer
    filterset_class = PostFilter
    # 필터 셋에 search filter 추가
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # 검색할 필드들 등록
    search_fields = ['post_title', 'post_content', 'post_introduce', 'user__username', 'created_at']

    # 쿼리 셋을 조작하기 위한 메소드
    def get_queryset(self):
        # 게시물 전부를 불러와 필터를 적용
        qs = self.filter_queryset(super().get_queryset())
        pk = self.kwargs.get('pk')
        qs = qs.filter(pk=pk)
        # 필터가 적용된 쿼리셋을 리턴
        return qs

# post detail
class PostDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.annotate(likes= Count('like', distinct=True), views = Count('view', distinct=True)).all()
    serializer_class = PostsSerializer

class PostsLikesAPIView(APIView):

    def get_object(self, pk):
        try:
            return Posts.objcets.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404
    def get(self,request, pk, format = None):
        like = self.get_object(pk=pk)
        serializer = PostsLikeSerializer
        return Response(serializer.data)

    def delete(self,request,pk,format = None):
        like = self.get_object(pk=pk)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)#?


class FamousPostsGenerics(generics.ListAPIView):
    # 포스트의 like 수와 view 수를 센다.(Count 함수 이용) annotate를 통해 필드 추가
    queryset = Posts.objects.annotate(likes= Count('like', distinct=True), views = Count('view', distinct=True)).all()
    serializer_class = PostsSerializer
    # 쿼리 셋을 재조정하기 위해 사용 왜냐하면 위에서는 url parameter를 못받기 때문에
    def get_queryset(self):
        # 위에 작성한 쿼리셋 가져오기
        qs = super().get_queryset()
        # url parameter 가져오기 ex) /api/posts/famous?order_by=-likes
        # 예시에 order_by 옆에 값을 가져온다.
        order_by = self.request.query_params.get('order_by', None)
        # 쓰여져 있는게 있는지 확인
        if order_by is not None:
            # -likes면 like 카운트 수의 내림차순으로 정렬
            if order_by == '-likes':
                qs = qs.order_by('-likes')
            # 그 외에는 -views 카운트 수의 내림차순으로 정렬
            else :
                qs = qs.order_by('-views')
        else:
            # 일반적으로는 like 카운트 수의 내림차순 정렬
            qs = qs.order_by('-likes')
        return qs
    # method가 get일 때 호출되는 함수
    def get(self, request, *args, **kargs):
        # mixins 상속으로 손쉽게 리스트 구현
        return self.list(self, request, *args, **kargs)
