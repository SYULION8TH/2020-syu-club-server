from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from club.serializers.intClubSerializers import IntClubsSerializer
from user.models import RelInterestClub, Clubs
from django.contrib.auth.models import AnonymousUser

class InterestClub(APIView):
    def get(self,request, pk):
        club_obj = RelInterestClub()
        club_obj.club = get_object_or_404(Clubs, pk = pk)
        if type(request.user) == AnonymousUser:
            club_obj.user = None
            return Response("Please Login First.", status = status.HTTP_400_BAD_REQUEST)
        else:
            club_obj.user = self.request.user

        club_obj.save()
        return Response('추가되었습니다.', status = status.HTTP_201_CREATED)


class InterestClubDetail(APIView):
    def get_object(self, pk):
        try:
            return RelInterestClub.objects.get(pk=pk)
        except:
            raise Http404 

    def delete(self, request, pk, format=None):
        club = self.get_object(pk)
        club.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
