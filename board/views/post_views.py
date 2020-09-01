from django.shortcuts import render
from django.http import Http404
from user.models import Posts, PostsLike, PostsViews
from rest_framework import generics, viewsets, mixins, status
from rest_framework.views import APIView
#경로를 표시하기 위해서는 . 단일파일이 아닌 폴더 형태기 때문에 경로 표시 필수
from board.serializers.post_serializers import PostsSerializer, PostsLikeSerializer
#filter을 사용
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import SearchFilter
from django.db.models import Count
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta


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
    search_fields = ['post_title', 'post_content', 'post_introduce', 'user__username']

    # 쿼리 셋을 조작하기 위한 메소드
    def get_queryset(self):
        # 게시물 전부를 불러와 필터를 적용
        qs = self.filter_queryset(super().get_queryset())
        pk = self.kwargs.get('pk')
        if pk == None:
            return qs
        qs = qs.filter(pk=pk)
        # 필터가 적용된 쿼리셋을 리턴
        return qs

# 요청자의 ip를 가져온다.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# post detail
class PostDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.annotate(likes= Count('like', distinct=True), views = Count('view', distinct=True)).all()
    serializer_class = PostsSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        flag = False
                # 현재시간
        now = datetime.now()
        # 현재에서 1시간 전
        yesterday = now - timedelta(hours=1)
        # 1시간 사이의 조회자들을 가져온다.
        postViews = PostsViews.objects.filter(checked_at__range = [yesterday, now], post=pk)
        # 1시간 사이의 조회 데이터를 살피고 1시간 내에 조회한 기록이 있으면 조회수를 추가하지 않는다.
        for item in postViews:
            if item.user_ip == get_client_ip(self.request):
                flag = True
        # 1시간 사이의 조회 데이터를 살피고 조회한 기록이 없으면 조회수 추가
        # 조회 데이터를 생성하기 위해 새로운 조회 객체 생성
        postView = PostsViews()
        # 객체의 post필드에 조회한 게시물 넣기
        # posts/:pk/view url 경로를 통해 pk 가져오기
        postView.post = get_object_or_404(Posts, pk = pk)
        # 로그인한 유저라면 요청한 유저를 객체의 유저 필드에 넣는다.
        if self.request.user.is_authenticated:
            postView.user = self.request.user
        # 로그인한 유저가 아니라면 객체의 유저 필드를 비워둔다.
        else:
            postView.user = None
        # 요청자의 ip를 기록한다.
        postView.user_ip = get_client_ip(self.request)
        # 만든 객체를 저장한다.
        if flag:
            pass
        else:
            postView.save()

        return super().get_queryset()

# 좋아요
class PostsLikesAPIView(APIView):

    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        # 로그인을 안했으면 401 에러를 발생시킨다. 
        if not request.user.is_authenticated:
            return Response("Please Login First", status = status.HTTP_401_UNAUTHORIZED)
	#post라는 객체 정의해서 posts models에 pk(primary key)르 가져옴
        # post = get_object_or_404(Posts, pk = pk)
        post = Posts.objects.filter(pk=pk)
        # post가 있을때
        if post.exists():
	#models를 가져옴
            post_like = PostsLike()
	        #pk를 post_like.posts에 정의
            post_like.posts = post[0]
	        # 요청받는 유저를 post_like.user에 정의
            post_like.user = request.user
            #좋아요가 이미 있을때 -> like.delete()
            if post[0].like.filter(user = request.user).exists():
                # post[0].like.remove(request.user)
                post[0].like.filter(user=request.user).delete()
	# 좋아요가 없을 때 create
            else:
                post[0].like.add(post_like.user)
                return post_like
            post_like.save()
            serializer = PostsLikeSerializer(post_like)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        # post가 없을때
        else:
            return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)
        temp = PostsLikeSerializer(post_like)
        serializer = PostsLikeSerializer(data = temp.data)

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
