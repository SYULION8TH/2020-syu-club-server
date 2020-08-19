from rest_framework import viewsets
from user.models import ClubsQna
from qna.serializers import qnaSerializers
from rest_framework.filters import SearchFilter


class QnaViewSet(viewsets.ModelViewSet):
    queryset = ClubsQna.objects.all()
    serializer_class = qnaSerializers.QnaSerializer

    filter_backends = [SearchFilter]
    search_fields = ('question_title',)
