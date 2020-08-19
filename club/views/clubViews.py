from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from club.serializers.clubSerializers import ClubsSerializer 
from user.models import Clubs
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
# from django_filters.rest_framework import DjangoFilterBackend, FilterSet

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


        
