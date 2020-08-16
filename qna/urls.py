from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import qnaviews
from .views import qnaCommentViews

router = DefaultRouter()
router.register('qna', qnaviews.QnaViewSet)
router.register('qnareplies', qnaCommentViews.QnaRepliesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]