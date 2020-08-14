from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from club.serializers.club_serializers import ClubsSerializer 
from user.models import Clubs

class ClubsList(APIView):
    def get(self, request, format=None):       
        clubs = Clubs.objects.all()
        serializer = ClubsSerializer(clubs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    
        
