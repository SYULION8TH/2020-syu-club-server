from rest_framework import generics, viewsets
from user.models import ClubsQna, QnaReplies, Clubs
from qna.serializers import qnaSerializers
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django.shortcuts import get_object_or_404

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

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        qs = super().get_queryset()
        qs = qs.filter(club = pk)
        return qs

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        club = get_object_or_404(Clubs, pk=pk)
        serializer.save(user = self.request.user, club = club)

class QnaDetail(generics.RetrieveUpdateDestroyAPIView):
<<<<<<< HEAD
    # queryset = ClubsQna.objects.all()
=======
>>>>>>> aaf47a07bcdad59fa6f04cf88008e6aa9b979a47
    queryset = ClubsQna.objects.all()
    serializer_class = qnaSerializers.QnaSerializer