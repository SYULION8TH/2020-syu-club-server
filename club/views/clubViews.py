from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework import status
from club.serializers.clubSerializers import ClubsSerializer, PostSerializer,PostLikeSerializer, FClubSerializer
from user.models import Clubs, Posts, PostsLike
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django.db import connection
from django.db.models import Count, F

class ClubfilterSet(FilterSet):
    class Meta:
        model = Clubs
        fields = {'club_name':['contains']}

class ClubsList(generics.GenericAPIView):
    queryset = Clubs.objects.all()
    serializer_class = ClubsSerializer    
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClubfilterSet

    def get(self, request): 
        clubs = self.filter_queryset(self.get_queryset())
        if clubs.exists():
            serializer = self.serializer_class(clubs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Returned empty queryset"}, status=status.HTTP_404_NOT_FOUND)  


class ClubDetail(APIView):
    def get_object(self, pk):
        try:
            return Clubs.objects.get(pk=pk)
        except Clubs.DoesNotExist:
            raise Http404    

    def get(self, request, pk, format=None):
        clubs_detail = self.get_object(pk)  
        serializer = ClubsSerializer(clubs_detail)  
        return Response(serializer.data)


        
class FamousClubList(generics.GenericAPIView):
    # query = Posts.objects.all()
    queryset = Posts.objects.values('club', 'post_id')   
    serializer_class = PostSerializer

    def get(self, request):
        clubs = Posts.objects.all()
        club_Posts = self.get_queryset()
        cats = {item['club'] for item in club_Posts}
        print(club_Posts)
        print(cats)
        post_likes = PostsLike.objects.all()
       
        if clubs.exists():
            serializer = self.serializer_class(clubs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Returned empty queryset"}, status=status.HTTP_404_NOT_FOUND)  

class FClubList(mixins.ListModelMixin, generics.GenericAPIView):
    # queryset = Posts.objects.values('club').annotate(like_count= Count('like'), club_id=F('club')).values('club_id', 'like_count').order_by('-like_count')
    # serializer_class = FClubSerializer
    queryset = Clubs.objects.annotate(post_count = Count('club_posts')).all()
    serializer_class = ClubsSerializer

    def get(self, request, *args, **kwargs):
        print(self.queryset)
        return self.list(request, *args, **kwargs)
