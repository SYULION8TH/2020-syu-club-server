from rest_framework import viewsets
from user.models import QnaReplies
from qna.serializers import qnaCommentSerializers


class QnaRepliesViewSet(viewsets.ModelViewSet):
    queryset = QnaReplies.objects.all()
    serializer_class = qnaCommentSerializers.QnaRepliesSerializer
