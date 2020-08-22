from django.urls import path, include
from django.contrib import admin
# from rest_framework.urlpatterns import format_suffix_patternss
from .views import qnaviews, qnaRepliesViews
from qna.serializers import qnaSerializers, qnaRepliesSerializers


urlpatterns = [
    path('qna/', qnaviews.QnaList.as_view()), 
    path('qna/<int:pk>/', qnaviews.QnaDetail.as_view()),
    path('qna/<int:pk>/qnareplies/', qnaRepliesViews.QnaRepliesList.as_view()),
]

# urlpatterns = format_suffix_patterns