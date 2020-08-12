from rest_framework import viewsets
from .models import QnaComment
from .selializer import QnaCommentSerializer


class QnaCommentViewSet(viewsets.ModelVewSet):
    queryset = QnaComment.object.all()
    serializer_class = QnaCommentSerializer
