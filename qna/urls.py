from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import qnaViews, qnaRepliesViews

router = DefaultRouter()
router.register('qna', qnaViews.QnaViewSet)
router.register('qnareplies', qnaRepliesViews.QnaRepliesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]