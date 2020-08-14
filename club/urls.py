from django.urls import path, include
from rest_framework.routers import DefaultRouter
from club.views import club_views

urlpatterns = [
    path('clubs/', club_views.ClubsList.as_view()),
    path('clubs/<int:pk>',club_views.ClubDetail.as_view()),
]