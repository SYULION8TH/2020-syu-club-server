from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from .views import qnaViews, qnaRepliesViews


urlpatterns = [
    path('clubs/<int:club_id>/qna/', qnaViews.QnaList.as_view()), #qna 목록
    # path('qna/', qnaViews.QnaList.as_view()), #qna 목록
    path('clubs/<int:club_id>/qna/<int:pk>/', qnaViews.QnaDetail.as_view()), #qna 상세
    path('qna/<int:pk>/qnareplies/', qnaRepliesViews.QnaRepliesList.as_view()), #qna 댓글
]

urlpatterns = format_suffix_patterns(urlpatterns)