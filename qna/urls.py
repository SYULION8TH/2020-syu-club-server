from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from .views import qnaViews, qnaRepliesViews


urlpatterns = [
    path('clubs/<int:pk>/qna', qnaViews.QnaList.as_view()), #qna 목록
    path('clubs/<int:club_id>/qna/<int:pk>', qnaViews.QnaDetail.as_view()),
    path('qna/<int:pk>/replies', qnaRepliesViews.QnaRepliesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)