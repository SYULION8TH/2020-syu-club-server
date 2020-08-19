from rest_framework import viewsets
from user.models import QnaReplies
from qna.serializers import qnaRepliesSerializers


class QnaRepliesViewSet(viewsets.ModelViewSet):
    queryset = QnaReplies.objects.all()
    serializer_class = qnaRepliesSerializers.QnaRepliesSerializer
