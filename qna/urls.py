from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import qnaviews, qnaRepliesViews

router = DefaultRouter()
router.register('qna', qnaviews.QnaViewSet)
router.register('qnareplies', qnaRepliesViews.QnaRepliesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('qna/<int:pk>', include(router.urls)),
]

