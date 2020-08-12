from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('qna', views.QnaViewSet)
router.register('qna_comment', views.Qna_CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]