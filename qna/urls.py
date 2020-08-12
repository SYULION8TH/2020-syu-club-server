from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import qnaViews

router = DefaultRouter()
router.register('clubsqna', qnaViews.QnaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]