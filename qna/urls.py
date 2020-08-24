from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from .views import qnaViews, qnaRepliesViews


urlpatterns = [
<<<<<<< HEAD
    path('clubs/<int:club_id>/qna/', qnaViews.QnaList.as_view()), #qna 목록
    # path('qna/', qnaViews.QnaList.as_view()), #qna 목록
    path('clubs/<int:club_id>/qna/<int:pk>/', qnaViews.QnaDetail.as_view()), #qna 상세
    path('qna/<int:pk>/qnareplies/', qnaRepliesViews.QnaRepliesList.as_view()), #qna 댓글
=======
    path('clubs/<int:pk>/qna/', qnaViews.QnaList.as_view()), #qna 목록
    path('clubs/<int:club_id>/qna/<int:pk>/', qnaViews.QnaDetail.as_view()),
    path('qna/<int:pk>/replies/', qnaRepliesViews.QnaRepliesList.as_view()),
>>>>>>> aaf47a07bcdad59fa6f04cf88008e6aa9b979a47
]

urlpatterns = format_suffix_patterns(urlpatterns)