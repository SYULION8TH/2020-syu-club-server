from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from club.serializers.intClubSerializers import IntClubsSerializer 
from user.models import RelInterestClub, Clubs

class InterestClub(APIView):

    def post(self, request,pk, format=None):
        intClub = get_object_or_404(Clubs, pk=pk)
        print(intClub)
        # if post.user.filter(username=request.user.username).exists():
        # post.user.remove(request.user)    
        # else:
        # post.user.add(request.user)
        serializer = IntClubsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      


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

    





