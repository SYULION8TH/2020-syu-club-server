from rest_framework import generics, viewsets
from user.models import QnaReplies, ClubsQna, Clubs
from qna.serializers import qnaRepliesSerializers
from django.shortcuts import get_object_or_404


class QnaRepliesList(generics.ListCreateAPIView): 
    serializer_class = qnaRepliesSerializers.QnaRepliesSerializer
    queryset = QnaReplies.objects.all()
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        qs = super().get_queryset()
        qs = qs.filter(question=pk)

    # def perform_create(self, serializer):
    #     pk = self.kwargs.get('pk')
    #     club = get_object_or_404(ClubsQna, pk=pk)
    #     serializer.save(user = self.request.user, club = club)


            # 1. 글 pk에 연관된 qna만 가져오기
            # 2. 로그인 한 내가, 관리자인지 알아보기
        if(self.request.user.is_superuser):
                # 2.1. 관리자라면, 다 읽어서 보여주기
            print("admin")
            return qs
        else :
                # 2.2. 관리자아니라면, 내가 쓴 댓글이 아니면서 / 비밀 댓글인 것 숨기기 
            print("is not admin")
            for item in qs:
                if(item.is_secret == 1 and self.request.user != item.user):
                    print (item)
                    item.qna_reply_content="비밀 글 입니다."
            return qs

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        question = get_object_or_404(ClubsQna, pk=pk)
        # serializer.save(user = self.request.user, question=question)
        serializer.save(user=self.request.user, question=question)


