from rest_framework import generics, viewsets
from user.models import ClubsQna, QnaReplies
from qna.serializers import qnaSerializers
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

class QnaFilter(FilterSet):
    class Meta:
        model = ClubsQna
        fields = {'question_title':['contains']}

class QnaList(generics.ListCreateAPIView):
    queryset = ClubsQna.objects.all()
    serializer_class = qnaSerializers.QnaSerializer
    filterset_class = QnaFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        qs = super().get_queryset()
        qs = qs.filter(club = pk)
        return qs

class QnaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClubsQna.objects.all()
    serializer_class = qnaSerializers.QnaSerializer