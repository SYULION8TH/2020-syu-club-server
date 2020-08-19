from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from club.serializers.intClubSerializers import intClubsSerializer 
from user.models import RelInterestClub

class interestClubList(APIView):
    def get(self, request, format=None):
        intClubs = RelInterestClub.objects.all()
        if intClubs.exists():
            serializer = intClubsSerializer(intClubs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Returned empty queryset"}, status=status.HTTP_404_NOT_FOUND)     

    # def post(self, request, format=None):
    #     serializer = intClubsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      


class interestClubDetail(APIView):
    def get_object(self, pk):
        try:
            return RelInterestClub.objects.get(pk=pk)
        except:
            raise Http404 

    def delete(self, request, pk, format=None):
        club = self.get_object(pk)
        club.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    





