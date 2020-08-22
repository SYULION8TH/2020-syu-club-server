from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework import status
from club.serializers.clubSerializers import ClubsSerializer, FamousClubSerializer, LikeSerializer
from user.models import Clubs, Posts, PostsLike
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
<<<<<<< HEAD
from django.db import connection
from django.db.models import Count

=======
>>>>>>> d9e8b73b1283633b5112d87292cc52d46443d3c7

class ClubfilterSet(FilterSet):
    class Meta:
        model = Clubs
        fields = {'club_name':['contains']}

class ClubsList(generics.GenericAPIView):
    queryset = Clubs.objects.all()
    serializer_class = LikeSerializer    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['club_name', 'club_desc', 'established', 'club_type__club_type_name', 'club_type__club_type_desc']
    filterset_class = ClubfilterSet

    def get(self, request):

        clubs = self.filter_queryset(self.get_queryset())
        if clubs.exists():
            serializer = self.serializer_class(clubs, many=True,context={'request': request})
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

class FamousClubList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Clubs.objects.raw('SELECT TEMP.club_id, COUNT(L.posts_like_id) as like_count FROM\
                 (SELECT C.club_id AS club_id, P.post_id as post_id, C.club_name AS club_name FROM\
                 clubs as C LEFT JOIN posts as P ON C.club_id = P.club_id) TEMP LEFT JOIN posts_like AS L \
                ON TEMP.post_id = L.posts_id GROUP BY TEMP.club_id order by like_count desc')
    serializer_class = FamousClubSerializer

    def get(self, request, *args, **kwargs):
        # print(self.queryset)
        return self.list(request, *args, **kwargs)
