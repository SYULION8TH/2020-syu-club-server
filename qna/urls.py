from django.urls import path, include
from django.contrib import admin
# from rest_framework.urlpatterns import format_suffix_patternss
from .views import qnaViews, qnaRepliesViews


urlpatterns = [
    path('qna/', qnaViews.QnaList.as_view()), #qna 목록
    path('qna/<int:pk>/', qnaViews.QnaDetail.as_view()),
    path('qna/<int:pk>/qnareplies/', qnaRepliesViews.QnaRepliesList.as_view()),
]

# urlpatterns = format_suffix_patterns