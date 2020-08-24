from rest_framework import generics, viewsets
from user.models import ClubsQna, QnaReplies
from qna.serializers import qnaSerializers
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django.shortcuts import render


# class QnaViewSet(viewsets.ModelViewSet):
#     queryset = ClubsQna.objects.all()
#     serializer_class = qnaSerializers.QnaSerializer

#     filter_backends = [SearchFilter]
#     search_fields = ('question_title',)

class QnaFilter(FilterSet):
    class Meta:
        model = ClubsQna
        fields = {'question_title':['contains']}

class QnaList(generics.ListCreateAPIView):
    queryset = ClubsQna.objects.all()
    serializer_class = qnaSerializers.QnaSerializer
    filterset_class = QnaFilter
    filter_backends = [DjangoFilterBackend]
    pk_url_kwarg = 'club_id'

    def get_queryset(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        qs = super().get_queryset()
        qs = qs.filter(club = pk)

        return qs

class QnaDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = ClubsQna.objects.all()
    queryset = ClubsQna.objects.all()
    serializer_class = qnaSerializers.QnaSerializer