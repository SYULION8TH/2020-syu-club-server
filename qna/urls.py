from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import qnaViews

router = DefaultRouter()
router.register('qna', qnaViews.QnaViewSet)
# router.register('qna_comment', views.Qna_CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]