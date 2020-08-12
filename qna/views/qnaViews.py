from rest_framework import viewsets
from user.models import ClubsQna
from qna.serializers import qnaSerializers


class QnaViewSet(viewsets.ModelViewSet):
    queryset = ClubsQna.objects.all()
    serializer_class = qnaSerializers.QnaSerializer
