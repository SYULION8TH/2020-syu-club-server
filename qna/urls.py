<<<<<<< HEAD
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from . import views

# router = DefaultRouter()
# router.register('qna', views.QnaViewSet)
# router.register('qna_comment', views.Qna_CommentViewSet)
=======
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import qnaViews

router = DefaultRouter()
router.register('clubsqna', qnaViews.QnaViewSet)

>>>>>>> b31b7653b082706c713ce9828b72ba7cbd5f0f34

# urlpatterns = [
#     path('', include(router.urls)),
# ]